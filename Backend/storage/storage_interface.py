from  Backend.storage.file_storage import FileStorage as store

STORAGE_LOCATION = "Backend/storage/data/"

class StorageInterface:
    def __init__(self, request:dict):
        self.request = request
        self.request_handler = {
            "CREATE": self.create_element,
            "RETRIEVE": self.retrieve_element,
            "UPDATE": self.update_element,
            "DELETE": self.delete_element
        }
        requesting_user = self.request.get("userUID",'0000') # defaults to user with no permissions
        self.storage = store(STORAGE_LOCATION, requesting_user)

    def request_parser(self):
        action = self.request.get("queryAction").upper()
        if action in self.request_handler:
            return self.request_handler[action]()
        else:
            return [{"error":"Unknown query action"}]

    def create_element(self):
        # TODO: integrate element classes to fill in gaps of passed in
        # data and standardize elements before creating
        try:
            element = self.request.get("queryElement", "")
            element_id = self.request.get("elementUID", "")
            element_info = self.request.get("newInfo", {})
            result = self.storage.create(element, element_id, element_info)
            return [{"result": result}]
        except AttributeError:
            return [{"result": f'element "{element}" doesn\'t exist'}]
        except PermissionError:
            action = self.request.get('queryAction')
            return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
        except NotImplementedError:
            action = self.request.get('queryAction')
            return [{"result": f'unable to {action} {element}:"{element_id}"'}]

    def retrieve_element(self):
        # TODO:
        # if element ID is "ALL" get all users and 
        # iterate to get each
        try:
            element = self.request.get("queryElement", "")
            element_id = self.request.get("elementUID", "")
            result = self.storage.retrieve(element, element_id)
            return [{element_id: result}]
        except AttributeError:
            return [{"result": f'element "{element}" doesn\'t exist'}]
        except PermissionError:
            action = self.request.get('queryAction')
            return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
        except NotImplementedError:
            action = self.request.get('queryAction')
            return [{"result": f'unable to {action} {element}:"{element_id}"'}]

    def update_element(self):
        try:
            element = self.request.get("queryElement", "")
            element_id = self.request.get("elementUID", "")
            element_info = self.request.get("newInfo", {})
            result = self.storage.update(element, element_id, element_info)
            return [{"result": result}]
        except AttributeError:
            return [{"result": f'element "{element}" doesn\'t exist'}]
        except PermissionError:
            action = self.request.get('queryAction')
            return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
        except NotImplementedError:
            action = self.request.get('queryAction')
            return [{"result": f'unable to {action} {element}:"{element_id}"'}]


    def delete_element(self):
        try:
            element = self.request.get("queryElement", "")
            element_id = self.request.get("elementUID", "")
            result = self.storage.delete(element, element_id)
            return [{"result": result}]
        except AttributeError:
            return [{"result": f'element "{element}" doesn\'t exist'}]
        except PermissionError:
            action = self.request.get('queryAction')
            return [{"result": f'invalid permissions to {action} {element}:"{element_id}"'}]
        except NotImplementedError:
            action = self.request.get('queryAction')
            return [{"result": f'unable to {action} {element}:"{element_id}"'}]
