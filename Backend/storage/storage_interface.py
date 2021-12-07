"""
Project: Project Management Tool
Team:    4
Author:  Michael Martinez
Course:  CSCI 3920

"""
import os
import time
import uuid

from storage.file_storage import FileStorage as Store
from models.user import User
from models.organization import Organization
from models.projects import Project

STORAGE_LOCATION = "storage/data/"
USER_ID_COUNT = 1
PROJECT_ID_COUNT = 1
MODELS = {
    "USER": User,
    "ORGANIZATION": Organization,
    "PROJECT": Project
}


class StorageInterface:
    """
    Interface between incoming requests and the storage mechanism
    
    """
    _request: dict
    _storage: Store

    def __init__(self, request: dict):
        self._request = request
        self._requesting_user = self._request.get("userUID", '0000')  # defaults to user with no permissions
        self._storage = Store(STORAGE_LOCATION, self._requesting_user)

    @property
    def request(self):
        return self._request

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, storage_dir: str):
        if os.path.exists(storage_dir):
            self._storage._file_storage_dir = storage_dir
        else:
            raise ValueError("location does not exist")

    def request_parser(self):
        """
        Handles requests to CREATE|RETRIEVE|UPDATE|DELETE elements for project
        management tool.
        
        """
###############################################################################
# CREATE ######################################################################
###############################################################################
        def create_element():
            """
            creates element of request using storage api

            """
            global USER_ID_COUNT, PROJECT_ID_COUNT
            # get element from request
            element = self._request.get("queryElement", "")
            element_info = self._request.get("newInfo", {})
            try:
                # create model with element info
                model = {}
                if element == "USER":
                    model = User(
                        id=str(USER_ID_COUNT).zfill(4),
                        firstName=element_info.get("firstName"),
                        lastName=element_info.get("lastName"),
                        email=element_info.get("email"),
                        username=element_info.get("username"),
                        password=element_info.get("password"),
                        admin=True if element_info.get("admin").lower() == "true" else False
                    )
                    USER_ID_COUNT += 1
                elif element == "ORGANIZATION":
                    random_id = str(uuid.uuid1()).split('-')[0]
                    model = Organization(
                        name=element_info.get("name"),
                        id=random_id
                    )
                elif element == "PROJECT":
                    model = Project(
                        id="P"+str(USER_ID_COUNT).zfill(4),
                        title=element_info.get("title"),
                        description=element_info.get("description"),
                        goals=element_info.get("goals", []),
                        tasks=element_info.get("tasks", []),
                        usersCanEdit=element_info.get("usersCanEdit", [self._requesting_user]),
                        usersCanView=element_info.get("usersCanView", []),
                        createdDate=time.strftime("%m/%d/%Y %H:%M:%S"),
                        createdBy=self._requesting_user
                    )

                element_id = model.id
                print()
                result = self.storage.create(element, element_id, model.__dict__())
                return [{"result": result}]

            except AttributeError as err:
                print("ERR|", err)
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError as err:
                print("ERR|", err)
                return [{"result": f'invalid permissions to {self._request.get("queryAction")} {element}:"{element_id}"'}]
            except NotImplementedError as err:
                print("ERR|", err)
                return [{"result": f'unable to {self._request.get("queryAction")} {element}:"{element_id}"'}]

###############################################################################
# RETRIEVE ####################################################################
###############################################################################
        def retrieve_element():
            """
            retrieves element of request using storage api

            """
            element = self._request.get("queryElement", "")
            element_id = self._request.get("elementUID", "")
            try:
                if element_id.upper() == "ALL":
                    results = []
                    element_ids = []
                    if element == "USER":
                        element_ids = self.storage.getAllUserIDs()
                    if element == "ORGANIZATION":
                        element_ids = self.storage.getAllOrganizationsIDs()
                    if element == "PROJECT":
                        element_ids = self.storage.getAllUserIDs()
                    for e_id in element_ids:
                        results.append(self.storage.retrieve(element, e_id))
                    return results
                result = self.storage.retrieve(element, element_id)
                return [{element_id: result}]
            except AttributeError:
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError:
                return [{"result": f'invalid permissions to {self._request.get("queryAction")} {element}:"{element_id}"'}]
            except NotImplementedError:
                return [{"result": f'unable to {self._request.get("queryAction")} {element}:"{element_id}"'}]

###############################################################################
# UPDATE ######################################################################
###############################################################################
        def update_element():
            """
            updates element of request using storage api

            """
            element = self._request.get("queryElement", "")
            element_id = self._request.get("elementUID", "")
            element_info = self._request.get("newInfo", {})
            try:
                result = self.storage.update(element, element_id, element_info)
                return [{"result": result}]
            except AttributeError:
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError:
                action = self._request.get('queryAction')
                return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
            except NotImplementedError:
                action = self._request.get('queryAction')
                return [{"result": f'unable to {action} {element}:"{element_id}"'}]

###############################################################################
# DELETE ######################################################################
###############################################################################
        def delete_element():
            """
            deletes element of request using storage api

            """
            element = self._request.get("queryElement", "")
            element_id = self._request.get("elementUID", "")
            try:
                result = self.storage.delete(element, element_id)
                return [{"result": result}]
            except AttributeError:
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError:
                return [{"result": f'invalid permissions to {self._request.get("queryAction")} {element}:"{element_id}"'}]
            except NotImplementedError:
                return [{"result": f'unable to {self._request.get("queryAction")} {element}:"{element_id}"'}]

###############################################################################
# ACTION HANDLING #############################################################
###############################################################################
        request_handler = {
            "CREATE": create_element,
            "RETRIEVE": retrieve_element,
            "UPDATE": update_element,
            "DELETE": delete_element
        }

        action = self._request.get("queryAction").upper()
        if action in request_handler:
            return request_handler[action]()
        else:
            return [{"error":"Unknown query action"}]

