import Backend.storage.file_storage as fs

class StorageInterface:
    def __init__(self, request:dict):
        self.request = request
        self.request_handler = {
            "CREATE": self.create_element,
            "RETRIEVE": self.retrieve_element,
            "UPDATE": self.update_element,
            "DELETE": self.delete_element
        }
        self.storage = fs.FileStorage("Backend/storage/data/","0001")

    def request_parser(self):
        action = self.request.get("queryAction").upper()
        if action in self.request_handler:
            return self.request_handler[action]()
        else:
            return [{"error":"Unknown query action"}]

    def create_element(self):
        try:
            element = self.request.get("queryElement", "")
            element_id = self.request.get("elementUID", "")
            element_info = self.request.get("newInfo", {})
            result = self.storage.create(element, element_id, element_info)
            return [{"result": result}]
        except AttributeError:
            return [{"result": f'element "{element}" doesn\'t exist'}]
        except PermissionError:
            return [{"result": f'invalid permissions to edit "{element}"'}]

    def retrieve_element(self):

        return [{
            "elementUID":"",
            "requestedInfo":{}
            }]

    def update_element(self):

        return [{"result":"update successful"}]

    def delete_element(self):

        return [{"result":"deletion successful"}]
