import socket
import json
from src import keys
from src.utils import colors
from src.utils.serialize import deserialize

class Client:
    def __init__(self, host, port):
        self.HOST = host # Server's host
        self.PORT = port

    def send(self, msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(msg.encode('UTF-8')) # sending bytes...
            data = s.recv(1024).decode('UTF-8') # receiving bytes...
        return json.loads(data)

    def handle_response(self, response, public_key):
        is_authentic = keys.verify(response['message'], deserialize(response['signature']), public_key)

        if not is_authentic:
            print(colors.wrap('red', "Response compromised. Exiting program!"))
            return

        if response['status'] == 200:
            print(colors.wrap('green', (response['message'])))
        else:
            print(colors.wrap('red', (response['message'])))

def local_client_factory():
    return Client("127.0.0.1", 5121)
