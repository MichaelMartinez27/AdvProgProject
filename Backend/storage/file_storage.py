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

    def update(self, element:str, element_uid:str, element_info:dict):
        if element == "USER":
            if self.user == element_uid or self._getUser(self.user).get("admin",False):
                if self._updateUser(element_uid, element_info):
                    return "user updated"
                raise NotImplementedError("user does not exsist")
            else:
                raise PermissionError("user does not have permission to update element")
        if element == "ORGANIZATION":
            org = self._getOrganization(element_uid)
            if org:
                if self.user in org.get("editors",[]):
                    if self._updateOrganization(element_uid,element_info):
                        return "organization updated"
                    raise NotImplementedError("could not update organization")
                else:
                    raise PermissionError("user does not have permission to update element")
            else:
                raise NotImplementedError("organization does not exsist")
        elif element == "PROJECT":
            proj = self._getProject(element_uid)
            if proj:
                if self.user in proj.get("editors",[]):
                    if self._updateProject(element_uid, element_info):
                        return "project updated"
                    raise NotImplementedError("could not update project")
                else:
                    raise PermissionError("user does not have permission to update element")
            else:
                raise NotImplementedError("project does not exsist")
        # TODO: update task from project by
        # 1. open project,
        # 2. convert to dict,
        # 3. iterate through tasks,
        # 4. if task unique id matches updateTask()
        # 5. resave project without task
        elif element == "TASK":
            proj = self._getProject("-".join(element_uid.split("-")[:2]))
            if proj:
                if self.user in proj.get("editors",[]):
                    if self._updateTask(element_uid):
                        return "project updated"
                    raise NotImplementedError("could not update task")
                else:
                    raise PermissionError("user does not have permission to update element")
            else:
                raise NotImplementedError("project does not exsist")
        else:
            raise AttributeError("element does not exsist")


    def delete(self, element:str, element_uid:dict):
        if element == "USER":
            if self._getUser(self.user).get("admin",False) or self.user == element_uid:
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
        try:
            with open(f'{self.file_storage_dir}users/{user_id}.json',
                    mode="w",
                    encoding='utf-8') as file:
                json.dump(user_info, file)
            return True
        except:
            return False

    def _createOrganization(self, org_id:str, creator_id:str, org_info: dict):
        try:
            if not os.path.exists(f'{self.file_storage_dir}organizations/{org_id}'):
                os.makedirs(f'{self.file_storage_dir}organizations/{org_id}')
                os.makedirs(f'{self.file_storage_dir}organizations/{org_id}/projects')
            if creator_id:
                with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                        mode="w",
                        encoding="utf-8") as file: 
                    json.dump([creator_id], file)
            with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                    mode="w",
                    encoding='utf-8') as file:
                json.dump(org_info, file)
            return True
        except:
            return False

    def _createProject(self, proj_id:str, proj_info:str):
        try:
            org_id, proj_id = tuple(proj_id.split("-"))
            if not os.path.exists(f'{self.file_storage_dir}organizations/{org_id}'):
                return False
            with open(f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json',
                        mode="w",
                        encoding="utf-8") as file:
                json.dump(proj_info, file)
            return True
        except:
            return False

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

    def _updateUser(self, user_id: str, user_update_info: dict):
        user = self._getUser(user_id)
        if user:
            for key, val in user_update_info.items():
                if key != "userUID":
                    user[key] = val
            if self._createUser(user_id, user):
                return True
        return False

    def _updateOrganization(self, org_id: str, org_update_info: dict):
        org = self._getOrganization(org_id)
        if org:
            for key, val in org_update_info.items():
                if key == "user":
                    with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                    mode="r",
                    encoding="utf-8") as file:
                        users = json.load(file)
                        users.append(val)
                        with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                        mode="w",
                        encoding="utf-8") as file:
                            json.dump(users,file)
                elif key == "users":
                    with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                    mode="r",
                    encoding="utf-8") as file:
                        users = json.load(file)
                        users += val
                        with open(f'{self.file_storage_dir}organizations/{org_id}/users.json',
                        mode="w",
                        encoding="utf-8") as file:
                            json.dump(users,file)
                elif key != "organizationUID":
                    if type(val) == list:
                        org[key] = list(org.get(key,[])) + val
                    elif type(org.get(key)) == list:
                        org[key] += [val]
                    else:
                        org[key] = val
            if self._createOrganization(org_id, None, org):
                return True
        return False

    def _updateProject(self, proj_id: str, proj_update_info: str):
        proj = self._getProject(proj_id)
        if proj:
            for key, val in proj_update_info.items():
                if key != "projectUID":
                    if type(val) == list:
                        proj[key] = list(proj.get(key,[])) + val
                    elif type(proj.get(key)) == list:
                        proj[key] += [val]
                    else:
                        proj[key] = val
            if self._createProject(proj_id, proj):
                return True
        return False

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

