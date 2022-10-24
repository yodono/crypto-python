import socket

class Client:
    def __init__(self, host, port):
        self.HOST = host # Server's host
        self.PORT = port

    def send(self, msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(msg.encode('UTF-8')) # sending bytes...
            data = s.recv(1024).decode('UTF-8') # receiving bytes...
        return data

def local_client_factory():
    return Client("127.0.0.1", 5121)
