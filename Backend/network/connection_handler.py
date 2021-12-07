from threading import Thread
from time import sleep
import json
import re
from storage.storage_interface import StorageInterface

BUFFER_SIZE = 1024


class ConnectionHandler(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("LOG|New connection added...")

    def run(self):
        try:
            print(f"LOG|Connected by {self.addr}...")
            data = None
            data = self.conn.recv(BUFFER_SIZE)
            if not data: return
            data = re.findall(r"{.+}",data.decode('utf-8'))[-1]
            if not data: return
            request = json.loads(data)
            print("LOG|Recieved data:\n", request)
            storage = StorageInterface(request)
            response = storage.request_parser()
            response = bytes(json.dumps(response),encoding="utf-8")
            sleep(2)
            self.conn.sendall(response)
            print(f"LOG|Sent back to client: {response}")
        except KeyboardInterrupt:
            print("LOG|Goodbye!")
        except IOError as e:
            print("ERR|closing connection due to error...")
            print("*"*50, e, "*"*50, sep = "\n")
        finally:
            self.conn.close()
            print("LOG|connection closed...")

