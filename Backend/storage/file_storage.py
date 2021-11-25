"""
Project: Project Manager
Team:    4
Author:  Michael Martinez
Course: CSCI 3920

"""
import json
import os
import shutil


class FileStorage:
    """
    Implementation of storing data in a folder/file structure.

    """
    _file_storage_dir: str
    _user:             str
    _user_admin:       str

    def __init__(self,db_dir:str, user_uid:str = None):
        self._file_storage_dir = db_dir
        self._user =            user_uid
        self._user_admin =      self.retrieve("USER",self.user).get("admin",False)

    @property
    def file_storage_dir(self):
        return self._file_storage_dir

    @property
    def user(self):
        return self._user

    @property
    def user_admin(self):
        return self._user_admin

    def create(self,element: str, element_id: str, element_info: dict):
        """
        Public method to create element (USER|ORGANIZATION|PROJECT) based on
        information passed in.

        """
        def createUser(user_id:str, user_info: dict):
            """
            Private method that handles creation of USER
            
            """
            try:
                with open(f'{self.file_storage_dir}users/{user_id}.json',
                        mode="w",
                        encoding='utf-8') as file:
                    json.dump(user_info, file)
                return True
            except:
                return False

        def createOrganization(org_id:str, creator_id:str, org_info: dict):
            """
            Private method that handles creation of ORGANIZATION
            
            """
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

        def createProject(proj_id:str, proj_info:str):
            """
            Private method that handles creation of PROJECT
            
            """
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

        if not self.user and element == "USER":
            return "user signed up"
        if self.user == "1111" or self._user_admin:
            if element == "USER":
                createUser(element_id, element_info)
                return "user created"
            elif element == "ORGANIZATION":
                createOrganization(element_id, self.user, element_info)
                return "org created"
            elif element == "PROJECT":
                if createProject(element_id, element_info):
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
        """
        Public method to retrieve element (USER|ORGANIZATION|PROJECT) based on
        unique id.

        """
        def getUser(user_id: str):
            """
            Private method that handles retrieval of USER
            
            """
            try:
                with open(f'{self.file_storage_dir}users/{user_id}.json',
                        mode="r",
                        encoding='utf-8') as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}

        def getOrganization(org_id: str):
            """
            Private method that handles retrieval of ORGANIZATION
            
            """
            try:
                with open(f'{self.file_storage_dir}organizations/{org_id}/info.json',
                        mode="r",
                        encoding='utf-8') as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}

        def getProject(proj_id: str):
            """
            Private method that handles retrieval of PROJECT
            
            """
            org_id, proj_id = tuple(proj_id.split("-"))
            try:
                with open(f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json',
                        mode="r",
                        encoding='utf-8') as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}

        if element == "PROJECT":
            project = getProject(element_uid)
            if project:
                if self.user in project.get("editors",[]) + project.get("viewers",[]):
                    return project
                raise PermissionError("user does not have permission to retrieve element")
            else:
                raise NotImplementedError("project does not exsist")
        elif element == "ORGANIZATION":
            org = getOrganization(element_uid)
            if org:
                if self.user in org.get("editors",[]) + org.get("viewers",[]):
                    return org
            else:
                raise NotImplementedError("orginization does not exsist")
        elif element == "USER" and (self.user == element_uid or self._user_admin):
            return getUser(element_uid)
        else:
            raise PermissionError("user does not have permission to retrieve element")

    def update(self, element:str, element_uid:str, element_info:dict):
        """
        Public method to update element (USER|ORGANIZATION|PROJECT) based on
        information passed in.

        """
        def updateUser(user_id: str, user_update_info: dict):
            """
            Private method that handles creation of USER
            
            """
            user = self.retrieve("USER",user_id)
            if user:
                for key, val in user_update_info.items():
                    if key != "userUID":
                        user[key] = val
                if self.create("USER",user_id, user):
                    return True
            return False

        def updateOrganization(org_id: str, org_update_info: dict):
            """
            Private method that handles update of ORGANIZATION
            
            """
            org = self.retrieve("ORGANIZATION",org_id)
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
                if self.create("ORGANIZATION",org_id, org):
                    return True
            return False

        def updateProject(proj_id: str, proj_update_info: str):
            """
            Private method that handles update of PROJECT
            
            """
            proj = self.retrieve("PROJECT",proj_id)
            if proj:
                for key, val in proj_update_info.items():
                    if key != "projectUID":
                        if type(val) == list:
                            proj[key] = list(proj.get(key,[])) + val
                        elif type(proj.get(key)) == list:
                            proj[key] += [val]
                        else:
                            proj[key] = val
                if self.create("PROJECT",proj_id, proj):
                    return True
            return False

        def updateTask():
            """
            Private method that handles update of TASK
            
            """
            # TODO:
            pass

        if element == "USER":
            if self.user == element_uid or self._user_admin:
                if updateUser(element_uid, element_info):
                    return "user updated"
                raise NotImplementedError("user does not exsist")
            else:
                raise PermissionError("user does not have permission to update element")
        if element == "ORGANIZATION":
            org = self.retrieve("ORGANIZATION",element_uid)
            if org:
                if self.user in org.get("editors",[]):
                    if updateOrganization(element_uid,element_info):
                        return "organization updated"
                    raise NotImplementedError("could not update organization")
                else:
                    raise PermissionError("user does not have permission to update element")
            else:
                raise NotImplementedError("organization does not exsist")
        elif element == "PROJECT":
            proj = self.retrieve("PROJECT",element_uid)
            if proj:
                if self.user in proj.get("editors",[]):
                    if updateProject(element_uid, element_info):
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
            proj = self.retrieve("PROJECT","-".join(element_uid.split("-")[:2]))
            if proj:
                if self.user in proj.get("editors",[]):
                    if updateTask(element_uid):
                        return "project updated"
                    raise NotImplementedError("could not update task")
                else:
                    raise PermissionError("user does not have permission to update element")
            else:
                raise NotImplementedError("project does not exsist")
        else:
            raise AttributeError("element does not exsist")


    def delete(self, element:str, element_uid:dict):
        """
        Public method to delete element (USER|ORGANIZATION|PROJECT) based on
        unique id.

        """
        def deleteUser(user_id: str):
            """
            Private method that handles deletion of USER
            
            """
            userfile = f'{self.file_storage_dir}users/{user_id}.json'
            if os.path.exists(userfile):
                os.remove(userfile)
                return True
            return False

        def deleteOrganization(org_id: str):
            """
            Private method that handles deletion of ORGANIZATION
            
            """
            orgfile = f'{self.file_storage_dir}organizations/{org_id}/'
            if os.path.exists(orgfile):
                shutil.rmtree(orgfile,ignore_errors=True)
                return True
            return False

        def deleteProject(proj_id: str):
            """
            Private method that handles deletion of PROJECT
            
            """
            org_id, proj_id = tuple(proj_id.split("-"))
            projfile = f'{self.file_storage_dir}organizations/{org_id}/projects/{proj_id}.json'
            if os.path.exists(projfile):
                os.remove(projfile)
                return True
            return False

        def deleteTask(task_id: str):
            """
            Private method that handles deletion of TASK
            
            """
            org_id, proj_id, task_id = tuple(task_id.split("-"))
            proj_id = "-".join([org_id,proj_id])
            project = self.retrieve("PROJECT", proj_id)
            for index, task in enumerate(project.get("tasks",[])):
                if task["id"] == task_id:
                    del (project["tasks"][index])
            if self.create("PROJECT", proj_id, project):
                return True
            return False

        if element == "USER":
            if self._user_admin or self._user == element_uid:
                if deleteUser(element_uid):
                    return "user deleted"
                raise NotImplementedError("user does not exsist")
            else:
                raise PermissionError("user does not have permission to delete element")
        if element == "ORGANIZATION":
            org = self.retrieve("ORGANIZATION",element_uid)
            if org:
                if self.user in org.get("editors",[]):
                    if deleteOrganization(element_uid):
                        return "organization deleted"
                    raise NotImplementedError("could not delete organization")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("organization does not exsist")
        elif element == "PROJECT":
            proj = self.retrieve("PROJECT",element_uid)
            if proj:
                if self.user in proj.get("editors",[]):
                    if deleteProject(element_uid):
                        return "project deleted"
                    raise NotImplementedError("could not delete project")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("project does not exsist")
        elif element == "TASK":
            proj = self.retrieve("PROJECT","-".join(element_uid.split("-")[:2]))
            if proj:
                if self.user in proj.get("editors",[]):
                    if deleteTask(element_uid):
                        return "project deleted"
                    raise NotImplementedError("could not delete task")
                else:
                    raise PermissionError("user does not have permission to delete element")
            else:
                raise NotImplementedError("project does not exsist")
        else:
            raise AttributeError("element does not exsist")

    def getAllUserIDs(self):
        """
        Public method to get all users saved in storage.

        """
        users = os.listdir(f'{self.file_storage_dir}users/')
        return [user.replace(".json","") for user in users]

    def getAllOrganizationsIDs(self):
        """
        Public method to get all organizations saved in storage.

        """
        organizations = os.listdir(f'{self.file_storage_dir}organizations/')
        return [organization.replace(".json","") for organization in organizations]

    def getAllProjectsIDs(self,organization_id):
        """
        Public method to get all projects saved in storage.

        """
        projects = os.listdir(f'{self.file_storage_dir}organizations/{organization_id}')
        return [project.replace(".json","") for project in projects]



