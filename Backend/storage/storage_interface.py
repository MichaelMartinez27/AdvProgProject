"""
Project: Project Management Tool
Team:    4
Author:  Michael Martinez
Course:  CSCI 3920

"""
import os
from  storage.file_storage import FileStorage as store

STORAGE_LOCATION = "Backend/storage/data/"

class StorageInterface:
    """
    Interface between incomming requests and the storage mechanism
    
    """
    _request: dict

    def __init__(self, request:dict):
        self._request = request
        requesting_user = self._request.get("userUID",'0000') # defaults to user with no permissions
        self._storage = store(STORAGE_LOCATION, requesting_user)

    @property
    def request(self):
        return self._request

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, storage_dir: str):
        if os.path.exists(storage_dir):
            self._storage = storage_dir
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
            # TODO: integrate element classes to fill in gaps of passed in
            # data and standardize elements before creating
            try:
                element = self._request.get("queryElement", "")
                element_id = self._request.get("elementUID", "")
                element_info = self._request.get("newInfo", {})
                # create model with element info
                # result = self.storage.create(element, element_id, dict(model))
                result = self.storage.create(element, element_id, element_info)
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
# RETRIEVE ####################################################################
###############################################################################
        def retrieve_element():
            """
            retrieves element of request using storage api

            """
            # TODO:
            # if element ID is "ALL" get all element and 
            # iterate to get each
            try:
                element = self._request.get("queryElement", "")
                element_id = self._request.get("elementUID", "")
                result = self.storage.retrieve(element, element_id)
                return [{element_id: result}]
            except AttributeError:
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError:
                action = self._request.get('queryAction')
                return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
            except NotImplementedError:
                action = self._request.get('queryAction')
                return [{"result": f'unable to {action} {element}:"{element_id}"'}]

###############################################################################
# UPDATE ######################################################################
###############################################################################
        def update_element():
            """
            updates element of request using storage api

            """
            try:
                element = self._request.get("queryElement", "")
                element_id = self._request.get("elementUID", "")
                element_info = self._request.get("newInfo", {})
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
            try:
                element = self._request.get("queryElement", "")
                element_id = self._request.get("elementUID", "")
                result = self.storage.delete(element, element_id)
                return [{"result": result}]
            except AttributeError:
                return [{"result": f'element "{element}" doesn\'t exist'}]
            except PermissionError:
                action = self._request.get('queryAction')
                return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
            except NotImplementedError:
                action = self._request.get('queryAction')
                return [{"result": f'unable to {action} {element}:"{element_id}"'}]

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

