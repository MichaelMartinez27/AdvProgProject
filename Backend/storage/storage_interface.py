

class StorageInterface:
    def __init__(self, request:dict):
        request = request
        request_handler = {
            "CREATE": self.create_element(),
            "RETRIEVE": self.retrieve_element(),
            "UPDATE": self.update_element(),
            "DELETE": self.delete_element()
        }

    def request_parser(self):
        action = self.request.get("queryAction").upper()
        if action in self.request_handler:
            return self.request_handler[action]()
        else:
            return [{"error":"Unknown query action"}]

    def create_element():
        return [{"result":"creation successful"}]

    def retrieve_element():
        return [{
            "elementUID":"",
            "requestedInfo":{}
            }]

    def update_element():
        return [{"result":"update successful"}]

    def delete_element():
        return [{"result":"deletion successful"}]
