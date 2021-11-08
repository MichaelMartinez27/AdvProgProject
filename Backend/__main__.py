from .network.server import Server

def main():
    server = Server("127.0.0.1",3920)
    server.run()

if __name__ == '__main__':
    main()