from threading import Thread
from time import sleep
import json
import re
from Backend.storage.storage_interface import StorageInterface

BUFFER_SIZE = 1024


class ConnectionHandler(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.storage = StorageInterface()
        print("LOG|New connection added...")

    def run(self):
        try:
            print(f"LOG|Connected by {self.addr}...")
            data = None
            data = self.conn.recv(BUFFER_SIZE)
            if not data: return
            data = re.findall(r"{.+}",data.decode('utf-8'))[-1]
            if not data: return
            data_dict = json.loads(data)
            print("\nRCV|Data:\t", data_dict)
            sleep(2)
            self.conn.sendall(b"DONE")
            print(f"Sent back to client: DONE")
        except KeyboardInterrupt:
            print("LOG|Goodbye!")
        except:
            print("ERR|closing connection due to error...")
        finally:
            self.conn.close()
            print("LOG|connection closed...")

