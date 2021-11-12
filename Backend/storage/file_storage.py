import json
import os

class FileStorage:
    def __init__(self,db_dir:str, user_uid:str = None):
        self.file_storage_dir = db_dir
        self.user = user_uid

    def create(self,element: str, element_id: str, element_info: dict):
        if not self.user and element == "USER":
            return "user signed up"
        if self._getUser(self.user)["admin"]:
            if element == "USER":
                self._createUser(element_id, element_info)
                return "user created"
            elif element == "ORGANIZATION":
                self._createOrganization(element_id, element_info)
                return "org created"
            elif element == "PROJECT":
                return "project created"
            elif element == "TASK":
                return "task for project created"
            else:
                raise AttributeError
        else:
            raise PermissionError

    def retrieve(self, element:str, element_uid:dict, filter:list[str]):
        if element == "PROJECT":
            project = self._getProject(element_uid)
            if self.user in project["editors"] + project["viewers"]:
                return {}
        elif element == "ORGANIZATION":
            org = self._getOrganization(element_uid)
            if self.user in org["editors"] + org["viewers"]:
                return {}
        elif element == "USER" and (self.user == element_uid or self._getUser(self.user)["admin"]):
            return {}
        else:
            raise PermissionError

    def update(self, element:str, element_uid:str, element_info:dict):
        if element == "PROJECT" and self.user in self._getProject(element_uid)["editors"]:
            return "project updated"
        if element == "TASK" and self.user in self._getProject(element_uid)["editors"]:
            return "task for project updated"
        if element == "USER" and (self.user == element_uid or self._getUser(self.user)["admin"]):
            return "user updated"
        if element == "ORGANIZATION" and self.user in self._getOrganization(element_uid)["editors"]:
            return "org updated"
        raise NotImplementedError


    def delete(self, element:str, element_uid:dict):
        if not self.user and element == "USER":
            return "user signed up"
        if self._getUser(self.user)["admin"]:
            if element == "USER":
                return "user deleted"
            elif element == "ORGANIZATION":
                return "org deleted"
            elif element == "PROJECT":
                return "project deleted"
            elif element == "TASK":
                return "task for project deleted"
            else:
                raise AttributeError
        else:
            raise PermissionError


    def _createUser(self, user_id:str, user_info: dict):
        with open(f'{self.file_storage_dir}users/{user_id}.json',
                  mode="w",
                  encoding='utf-8') as file:
            json.dump(user_info, file)


    def _createOrganization(self, org_id:str, org_info: dict):
        if not os.path.exists(f'{self.file_storage_dir}organizations/{org_id}'):
            os.makedirs(f'{self.file_storage_dir}organizations/{org_id}')
            os.makedirs(f'{self.file_storage_dir}organizations/{org_id}/projects')
        with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                  mode="w"): pass
        with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                  mode="w",
                  encoding='utf-8') as file:
            json.dump(org_info, file)


    def _createProject(self, project_id:str):
        pass


    def _updateDataForUser(self):
        pass


    def _updateDataForOrganization(self):
        pass


    def _getOrganization(self):
        pass


    def _updateOrganization(self):
        pass


    def _deleteOrganization(self):
        pass


    def _getAllUsers(self):
        pass


    def _getUser(self, user_id: str):
        return {"admin":True}


    def _updateUser(self):
        pass


    def _deleteUser(self):
        pass
