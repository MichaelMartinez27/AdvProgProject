from models.task import Task
from models.user import User


class Project:
    tasks = []

    def __init__(self, id, title, description, goals, tasks, usersCanEdit, usersCanView, createdDate, createdBy):
        self.id = id
        self.title = title
        self.description = description
        self.goals = goals
        self.tasks = tasks
        self.usersCanEdit = usersCanEdit
        self.usersCanView = usersCanView
        self.createdDate = createdDate
        self.createdBy = createdBy

    def __dict__(self):
        return {
            "Id" : self.id,
            "Title" : self.title,
            "Description": self.description,
            "Goals" : self.goals,
            "Tasks" : self.tasks,
            "Users Can Edit" : self.usersCanEdit,
            "Users Can View" : self.usersCanView,
            "Created Date": self.createdDate,
            "Created By" : self.createdBy
        }

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title

    def setTitle(self, titleName):
        self.title = titleName

    def getDescription(self):
        return self.description

    def setDescription(self, describe):
        self.description = describe

    def getGoals(self):
        return self.goals

    def setGoals(self, goal):
        self.goals = goal

    def getTasks(self):
        pass

    def getTask(self):
        pass

    def updateTask(self, id, name, description, status):
        newTask = Task(id, name, description, status)
        self.tasks.append(newTask)

    def deleteTask(self, deletedTaskName):
        if deletedTaskName in self.tasks:
            index = self.tasks.index(deletedTaskName)
            self.tasks.pop(index)

    def getTitle(self):
        return self.title

    def setTitle(self, titleName):
        self.title = titleName

    def addUser(self, fName, lName, email, userName, passWord):
        newUser = User(fName, lName, email, userName, passWord)
