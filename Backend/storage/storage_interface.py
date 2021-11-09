

class StorageInterface:
    def __init__(self, request:dict):
        self.request = request
        self.request_handler = {
            "CREATE": self.create_element,
            "RETRIEVE": self.retrieve_element,
            "UPDATE": self.update_element,
            "DELETE": self.delete_element
        }

    def request_parser(self):
        action = self.request.get("queryAction").upper()
        if action in self.request_handler:
            return self.request_handler[action]()
        else:
            return [{"error":"Unknown query action"}]

    def create_element(self):

        return [{"result":"creation successful"}]

    def retrieve_element(self):

        return [{
            "elementUID":"",
            "requestedInfo":{}
            }]

    def update_element(self):

        return [{"result":"update successful"}]

    def delete_element(self):

        return [{"result":"deletion successful"}]
