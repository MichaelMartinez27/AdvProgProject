from storage_interface import StorageInterface


def test():
    store_interface = StorageInterface({
        "userUID":"1111",
        "queryAction": "CREATE",
        "queryElement": "USER",
        "elementUID": "0001",
        "newInfo": {
            "username": "hello.world",
            "first":    "Michael",
            "last":     "Martinez",
            "email":    "foo.bar@gmail.com",
            "admin":    True
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "USER",
        "elementUID": "0001"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "CREATE",
        "queryElement": "ORGANIZATION",
        "elementUID":   "1234",
        "newInfo": {
            "name": "CompanyX",
            "users":    ["0001"],
            "editors":    ["0001"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "CREATE",
        "queryElement": "USER",
        "elementUID": "0002",
        "newInfo": {
            "username": "foo.bar",
            "first":    "John",
            "last":     "Doe",
            "email":    "jd@gmail.com",
            "admin":    False
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"1111",
        "queryAction": "CREATE",
        "queryElement": "USER",
        "elementUID": "0003",
        "newInfo": {
            "username": "jsmith123abc",
            "first":    "Jane",
            "last":     "Smith",
            "email":    "jane.smith@gmail.com",
            "admin":    False
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "CREATE",
        "queryElement": "ORGANIZATION",
        "elementUID": "5678",
        "newInfo": {
            "name": "CompanyY",
            "users":    ["0001","0002","0003"],
            "editors":    ["0001","0002"],
            "viewers":     ["0003"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"1111",
        "queryAction": "CREATE",
        "queryElement": "PROJECT",
        "elementUID": "1234-000010",
        "newInfo": {
            "title": "ProjectX",
            "description":  "The ultimate project!",
            "goals":        ["Acomplish this.","Work hard and fast."],
            "editors":      ["0001","0002"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "CREATE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000001",
        "newInfo": {
            "title": "Project Cold",
            "description":  "The coolest project ever!",
            "goals":        ["Simple goal."],
            "editors":      ["0001"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0002",
        "queryAction": "CREATE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000002",
        "newInfo": {
            "title": "Project Heat",
            "description":  "The hottest project ever!",
            "goals":        ["Acomplish all goals.","goal"],
            "editors":      ["0002","0003"],
            "viewers":      ["0001"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "UPDATE",
        "queryElement": "USER",
        "elementUID": "0002",
        "newInfo": {
            "admin":    True
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0002",
        "queryAction": "CREATE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000002",
        "newInfo": {
            "title": "Project Heat",
            "description":  "The hottest project ever!",
            "goals":        ["Acomplish all goals.","goal"],
            "editors":      ["0002","0003"],
            "viewers":      ["0001"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "USER",
        "elementUID": "0002"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "USER",
        "elementUID": "0003"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "ORGANIZATION",
        "elementUID": "1234"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "ORGANIZATION",
        "elementUID": "5678"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "PROJECT",
        "elementUID": "1234-000010"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000001"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "UPDATE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000001",
        "newInfo": {
            "goals":    ["Another simple goal","Complex goal"]
        }
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000001"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":      "0001",
        "queryAction":  "RETRIEVE",
        "queryElement": "PROJECT",
        "elementUID": "5678-000002"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0002",
        "queryAction": "DELETE",
        "queryElement": "USER",
        "elementUID": "0003"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0003",
        "queryAction": "DELETE",
        "queryElement": "ORGANIZATION",
        "elementUID": "1234"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0003",
        "queryAction": "DELETE",
        "queryElement": "ORGANIZATION",
        "elementUID": "5678"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "USER",
        "elementUID": "0002"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "USER",
        "elementUID": "0003"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "ORGANIZATION",
        "elementUID": "1234"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "ORGANIZATION",
        "elementUID": "1234"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "ORGANIZATION",
        "elementUID": "5678"
    })
    print(store_interface.request_parser())

    store_interface = StorageInterface({
        "userUID":"0001",
        "queryAction": "DELETE",
        "queryElement": "USER",
        "elementUID": "0001"
    })
    print(store_interface.request_parser())


if __name__ == '__main__':
    test()
