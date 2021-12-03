class Task:
    
    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def __dict__(self):
        return {
            "Id" : self.id,
            "Name" : self.name,
            "Description": self.description,
            "Status" : self.status
        }
        
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, nameUsed):
        self.name = nameUsed
    
    def getDescription(self):
        return self.description

    def setDescription(self, describe):
        self.description = describe

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status