import os

from file_storage import FileStorage
import os

FILE_STORAGE = "storage/data/"

def test():
    print(os.getcwd())
    store = FileStorage(FILE_STORAGE,"1111")
    print("LOGGED IN | 1111")
    print(store.create("USER","0001",{"first":"Michael","last":"Martinez","admin":True}))
    store = FileStorage(FILE_STORAGE,"0001")
    print("LOGGED IN | 0001")
    print(store.update("USER","0001",{"email":"michael.martinez@email.com"}))
    print(store.create("ORGANIZATION","1234",{"name":"CompanyX","editors":["0001"]}))
    print(store.retrieve("ORGANIZATION","1234"))
    print(store.create("USER","0002",{"first":"John","last":"Smith","admin":True}))
    print(store.retrieve("USER","0002"))
    print(store.update("USER","0002",{"email":"john.smith@email.com"}))
    print(store.retrieve("USER","0002"))
    print(store.create("ORGANIZATION","5678",{"name":"CompanyY","editors":["0001","0002"]}))
    print(store.create("PROJECT","1234-4321",{"title":"ProjectX","editors":["0001"]}))
    print(store.create("PROJECT","5678-4321",{"title":"ProjectA","editors":["0001","0002"]}))
    print(store.create("PROJECT","5678-8765",{"title":"ProjectB","editors":["0002"]}))
    print(store.retrieve("USER","0001"))
    print(store.retrieve("ORGANIZATION","1234",))
    print(store.retrieve("PROJECT","1234-4321"))
    print(store.update("PROJECT","1234-4321",{"description":"This is a cool project"}))
    print(store.retrieve("PROJECT","1234-4321"))
    print(store.retrieve("PROJECT","5678-4321"))
    print(store.update("PROJECT","5678-4321",{"description":"Another project.. blah","goals":["Do something","do something else"]}))
    print(store.retrieve("PROJECT","5678-4321"))
    print(store.delete("PROJECT","5678-4321"))
    try:
        print(store.retrieve("PROJECT","5678-4321"))
        print("*** Error should have been raised ***")
    except NotImplementedError as nie:
        print("Error correctly raised |->",nie)
    store = FileStorage(FILE_STORAGE,"0002")
    print("LOGGED IN | 0002")
    print(store.delete("PROJECT","5678-8765"))
    print(store.delete("ORGANIZATION","5678"))
    store = FileStorage(FILE_STORAGE,"0001")
    print("LOGGED IN | 0001")
    print(store.create("USER","0003",{"first":"John","last":"Doe","admin":False}))
    print(store.update("USER","0003",{"email":"jd@hotmail.com","username":"johnny-boi"}))
    print(store.retrieve("USER","0003"))
    print(store.update("ORGANIZATION","1234",{"users":["0002","0003"],"editors":"0003"}))
    print(store.retrieve("ORGANIZATION","1234"))
    print(store.delete("USER","0002"))
    store = FileStorage(FILE_STORAGE,"0003")
    print("LOGGED IN | 0003")
    try:
        print(store.delete("USER","0001"))
        print("*** Error should have been raised ***")
    except PermissionError as pe:
        print("Error correctly raised |->",pe)
    store = FileStorage(FILE_STORAGE,"0001")
    print("LOGGED IN | 0001")
    print(store.delete("ORGANIZATION","1234"))
    print(store.delete("USER","0003"))
    print(store.delete("USER","0001"))


if __name__ == '__main__':
    test()
