from threading import Thread
from time import sleep
import socket
import json
import re

from Backend.storage.StorageInterface import StorageInterface

BUFFER_SIZE = 1024

class Server():
    def __init__(self, addr: str, port: int) -> None:
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        try:
            print(f"LOG|Running on {self.addr}:{self.port}...")
            self.sock.bind((self.addr,self.port))
            while True:
                print("\nLOG|Waiting for client request...")
                self.sock.listen(1)
                conn, address = self.sock.accept()
                new_connection = ConnectionHandler(conn, address)
                new_connection.start()

        except KeyboardInterrupt:
            print("ERR|Closing server...")
        finally:
            self.sock.close()
            print("LOG|Server closed...")

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
            while True:
                data = self.conn.recv(BUFFER_SIZE)
                if not data: break
                data = re.findall(r"{.+}",data.decode('utf-8'))[-1]
                if not data: break
                data_dict = json.loads(data)
                print("CON|Data:\t", data_dict)
                sleep(10)
                self.conn.sendall(b"DONE")
        except:
            print("ERR|closing connection due to error...")
        finally:
            self.conn.close()
            print("LOG|connection closed...")



if __name__ == '__main__':
    # for testing
    s = Server("127.0.0.1", 80)
    s.run()