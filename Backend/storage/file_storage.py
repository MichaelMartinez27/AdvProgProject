import json
import os
import shutil

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
                    raise AttributeError("organization does not exsist")
            elif element == "TASK":
                return "task for project created"
            else:
                raise AttributeError("element does not exsist")
        else:
            raise PermissionError("user does not have permission to create element")

    def retrieve(self, element:str, element_uid:str):
        if element == "PROJECT":
            project = self._getProject(element_uid)
            if project:
                if self.user in project.get("editors",[]) + project.get("viewers",[]):
                    return project
                raise PermissionError("user does not have permission to retrieve element")
            else:
                raise NotImplementedError("project does not exsist")
        elif element == "ORGANIZATION":
            org = self._getOrganization(element_uid)
            if org:
                if self.user in org.get("editors",[]) + org.get("viewers",[]):
                    return org
            else:
                raise NotImplementedError("orginization does not exsist")
        elif element == "USER" and (self.user == element_uid or self._getUser(self.user).get("admin",False)):
            return self._getUser(element_uid)
        else:
            raise PermissionError("user does not have permission to retrieve element")

    # TODO: implement update by:
    # 1. retrieving element,
    # 2. converting to dict, 
    # 3. update dict,
    # 4. re-save updated dict
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
        if element == "USER":
            if self._getUser(self.user).get("admin",False):
                if self._deleteUser(element_uid):
                    return "user deleted"
                raise NotImplementedError("user does not exsist")
            else:
                raise PermissionError("user does not have permission to delete element")
        if element == "ORGANIZATION":
            org = self._getOrganization(element_uid)
            if org:
                if self.user in org.get("editors",[]):
                    if self._deleteOrganization(element_uid):
                        return "organization deleted"
                    raise NotImplementedError("could not delete organization")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("organization does not exsist")
        elif element == "PROJECT":
            proj = self._getProject(element_uid)
            if proj:
                if self.user in proj.get("editors",[]):
                    if self._deleteProject(element_uid):
                        return "project deleted"
                    raise NotImplementedError("could not delete project")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("project does not exsist")
        # TODO: delete task from project by
        # 1. open project,
        # 2. convert to dict,
        # 3. iterate through tasks,
        # 4. if task unique id matches del()
        # 5. resave project without task
        elif element == "TASK":
            proj = self._getProject("-".join(element_uid.split("-")[:2]))
            if proj:
                if self.user in proj.get("editors",[]):
                    if self._deleteTask(element_uid):
                        return "project deleted"
                    raise NotImplementedError("could not delete task")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("project does not exsist")
        else:
            raise AttributeError("element does not exsist")

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

    def _getUser(self, user_id: str):
        try:
            with open(f'{self.file_storage_dir}users/{user_id}.json',
                    mode="r",
                    encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _getOrganization(self, org_id: str):
        try:
            with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                    mode="r",
                    encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _getProject(self, proj_id: str):
        org_id, proj_id = tuple(proj_id.split("-"))
        try:
            with open(f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json',
                    mode="r",
                    encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _updateUser(self):
        # TODO:
        pass

    def _updateOrganization(self):
        # TODO:
        pass

    def _updateProject(self):
        # TODO:
        pass

    def _updateTask(self):
        # TODO:
        pass

    def _deleteUser(self, user_id: str):
        userfile = f'{self.file_storage_dir}users/{user_id}.json'
        if os.path.exists(userfile):
            os.remove(userfile)
            return True
        return False

    def _deleteOrganization(self, org_id: str):
        orgfile = f'{self.file_storage_dir}organizations/{org_id}/'
        if os.path.exists(orgfile):
            shutil.rmtree(orgfile,ignore_errors=True)
            return True
        return False

    def _deleteProject(self, proj_id: str):
        org_id, proj_id = tuple(proj_id.split("-"))
        projfile = f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json'
        if os.path.exists(projfile):
            os.remove(projfile)
            return True
        return False

    def _deleteTask(self,task_id: str):
        # TODO:
        pass


if __name__ == '__main__':
        store = FileStorage("Backend/storage/data/","1111")
        print("LOGGED IN | 1111")
        print(store.create("USER","0001",{"first":"Michael","last":"Martinez","admin":True}))
        store = FileStorage("Backend/storage/data/","0001")
        print("LOGGED IN | 0001")
        print(store.create("ORGANIZATION","1234",{"name":"CompanyX","editors":["0001"]}))
        print(store.create("USER","0002",{"first":"John","last":"Smith","admin":True}))
        print(store.create("ORGANIZATION","5678",{"name":"CompanyY","editors":["0001","0002"]}))
        print(store.create("PROJECT","1234-4321",{"title":"ProjectX","editors":["0001","0001"]}))
        print(store.create("PROJECT","5678-4321",{"title":"ProjectA","editors":["0001","0002"]}))
        print(store.create("PROJECT","5678-8765",{"title":"ProjectB","editors":["0002"]}))
        print(store.retrieve("USER","0001"))
        print(store.retrieve("ORGANIZATION","1234",))
        print(store.retrieve("PROJECT","1234-4321"))
        print(store.retrieve("PROJECT","5678-4321"))
        print(store.delete("PROJECT","5678-4321"))
        try:
            print(store.retrieve("PROJECT","5678-4321"))
            print("** Error should have been raised **")
        except NotImplementedError as nie:
            print("Error correctly raised |",nie)
        store = FileStorage("Backend/storage/data/","0002")
        print("LOGGED IN | 0002")
        print(store.delete("PROJECT","5678-8765"))
        print(store.delete("ORGANIZATION","5678"))
        store = FileStorage("Backend/storage/data/","0001")
        print("LOGGED IN | 0001")
        print(store.create("USER","0003",{"first":"John","last":"Doe","admin":False}))
        print(store.delete("USER","0002"))
        store = FileStorage("Backend/storage/data/","0003")
        print("LOGGED IN | 0003")
        try:
            print(store.delete("USER","0001"))
            print("** Error should have been raised **")
        except PermissionError as pe:
            print("Error correctly raised |",pe)
        store = FileStorage("Backend/storage/data/","0001")
        print("LOGGED IN | 0001")
        print(store.delete("ORGANIZATION","1234"))
        print(store.delete("USER","0003"))
