import json
import os

class FileStorage:
    def __init__(self,db_dir:str, user_uid:str = None):
        self.file_storage_dir = db_dir
        self.user = user_uid

    def create(self,element: str, element_id: str, element_info: dict):
        if not self.user and element == "USER":
            return "user signed up"
        if self.user == "1111" or self._getUser(self.user).get("admin",False):
            if element == "USER":
                self._createUser(element_id, element_info)
                return "user created"
            elif element == "ORGANIZATION":
                self._createOrganization(element_id, self.user, element_info)
                return "org created"
            elif element == "PROJECT":
                if self._createProject(element_id, element_info):
                    return "project created"
                else:
                    raise AttributeError("organiztion does not exsist")
            elif element == "TASK":
                return "task for project created"
            else:
                raise AttributeError("element does not exsist")
        else:
            raise PermissionError("user does not have permission to create element")

    def retrieve(self, element:str, element_uid:dict, filter:list[str]):
        if element == "PROJECT":
            project = self._getProject(element_uid)
            if self.user in project.get("editors",[]) + project.get("viewers",[]):
                return project
            raise PermissionError("user does not have permission to retrieve element")
        elif element == "ORGANIZATION":
            org = self._getOrganization(element_uid)
            if self.user in org.get("editors",[]) + org.get("viewers",[]):
                return org
        elif element == "USER" and (self.user == element_uid or self._getUser(self.user).get("admin",False)):
            return self._getUser(element_uid)
        else:
            raise PermissionError

    def update(self, element:str, element_uid:str, element_info:dict):
        if element == "PROJECT" and self.user in self._getProject(element_uid).get("editors",[]):
            return "project updated"
        if element == "TASK" and self.user in self._getProject(element_uid).get("editors",[]):
            return "task for project updated"
        if element == "USER" and (self.user == element_uid or self._getUser(self.user).get("admin",False)):
            return "user updated"
        if element == "ORGANIZATION" and self.user in self._getOrganization(element_uid).get("editors",[]):
            return "org updated"
        raise NotImplementedError


    def delete(self, element:str, element_uid:dict):
        if not self.user and element == "USER":
            return "user signed up"
        if self._getUser(self.user).get("admin",False):
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

    def getAllUserIDs(self):
        users = os.listdir(f'{self.file_storage_dir}users/')
        return [user.replace(".json","") for user in users]

    def _createUser(self, user_id:str, user_info: dict):
        with open(f'{self.file_storage_dir}users/{user_id}.json',
                  mode="w",
                  encoding='utf-8') as file:
            json.dump(user_info, file)


    def _createOrganization(self, org_id:str, creator_id:str, org_info: dict):
        if not os.path.exists(f'{self.file_storage_dir}organizations/{org_id}'):
            os.makedirs(f'{self.file_storage_dir}organizations/{org_id}')
            os.makedirs(f'{self.file_storage_dir}organizations/{org_id}/projects')
        with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                  mode="w",
                  encoding="utf-8") as file: 
            json.dump([creator_id], file)
        with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                  mode="w",
                  encoding='utf-8') as file:
            json.dump(org_info, file)


    def _createProject(self, proj_id:str, proj_info:str):
        org_id, proj_id = tuple(proj_id.split("-"))
        if not os.path.exists(f'{self.file_storage_dir}organizations/{org_id}'):
            return False
        with open(f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json',
                    mode="w",
                    encoding="utf-8") as file:
            json.dump(proj_info, file)
        return True

    def _updateDataForUser(self):
        pass


    def _updateDataForOrganization(self):
        pass


    def _getOrganization(self,org_id:str):
        with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                  mode="r",
                  encoding='utf-8') as file:
            return json.load(file)


    def _updateOrganization(self):
        pass


    def _deleteOrganization(self):
        pass


    def _getUser(self, user_id: str):
        with open(f'{self.file_storage_dir}users/{user_id}.json',
                  mode="r",
                  encoding='utf-8') as file:
            return json.load(file)


    def _updateUser(self):
        pass


    def _deleteUser(self):
        pass

    def _getProject(self,proj_id: str):
        org_id, proj_id = tuple(proj_id.split("-"))
        with open(f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json',
                  mode="r",
                  encoding='utf-8') as file:
            return json.load(file)


if __name__ == '__main__':
        store = FileStorage("Backend/storage/data/","1111")
        print(store.create("USER","0001",{"first":"Michael","admin":True}))
        store = FileStorage("Backend/storage/data/","0001")
        print(store.create("ORGANIZATION","1234",{"name":"CompanyX","editors":["0001"]}))
        print(store.create("ORGANIZATION","5678",{"name":"CompanyY","editors":["0001","0002"]}))
        print(store.create("PROJECT","1234-4321",{"title":"ProjectX","editors":["0001","0001"]}))
        print(store.create("PROJECT","5678-4321",{"title":"ProjectA","editors":["0001","0002"]}))
        print(store.create("PROJECT","5678-8765",{"title":"ProjectB","editors":["0002"]}))
        print(store.retrieve("USER","0001",{}))
        print(store.retrieve("ORGANIZATION","1234",{}))
        print(store.retrieve("PROJECT","1234-4321",{}))
        print(store.retrieve("PROJECT","5678-4321",{}))
