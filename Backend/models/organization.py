from user import User
from projects import Project

class Organization:
    
    users = []
    projects = []

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __dict__(self):
        
        return {
            "Name" : self.name,
            "Id" : self.id
        }

    def getId(self):
        return self.id
    
    def addUser(self, fName, lName, email, userName, passWord):
        newUser = User(fName, lName, email, userName, passWord)
        self.users.append(newUser)

    def addProject(self, id, title, description, goals, tasks, usersCanEdit, usersCanView, createdDate, createdBy):
        newProject = Project(id, title, description, goals, tasks, usersCanEdit, usersCanView, createdDate, createdBy)
        self.projects.append(newProject)
        
    def getUser(self, userName):
        if userName in self.users:
            index = self.users.index(userName)
        
        return self.users[index]
        
    def getUsers(self):
        
        return self.users
    
    def getProject(self, findProject):
        
        if findProject in self.projects:
            index = self.projects.index(findProject)
        
        return self.projects[index]
        
    def getProjects(self):
        
        return self.projects
    
    def deleteUser(self, findNameOfUser):
        
        if findNameOfUser in self.users:
            index = self.users.index(findNameOfUser)
            self.users.pop(index)
            
    def deleteProject(self, findProjectTitle):
        
        if findProjectTitle in self.projects:
            index = self.projects.index(findProjectTitle)
            self.projects.pop(index)
    
