import socket
from Backend.network.connection_handler import ConnectionHandler

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
                new_connection.daemon = True
                new_connection.start()
        except KeyboardInterrupt:
            print("ERR|Closing server...")
        finally:
            self.sock.close()
            print("LOG|Server closed...")



if __name__ == '__main__':
    # for testing
    s = Server("127.0.0.1", 80)
    s.run()