import socket
import json
from src import keys
from src.utils.serialize import serialize

class Server:
    def __init__(self, host, port, public_key, private_key, symmetric_key):
        self.HOST = host  # Server's host
        self.PORT = port
        self.public_key = public_key
        self.private_key = private_key
        self.symmetric_key = symmetric_key

    # socket.AF_INET: IPv4
    # socket.SOCK_STREAM: TCP
    def run(self, router):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.HOST, self.PORT))
                s.listen()
                conn, addr = s.accept() # provides client socket and address

                with conn:
                    print(f"Connected by {addr}")

                    while True:
                        data = conn.recv(1024).decode('UTF-8')

                        if not data:
                            break
                        req = router.parse(data, self.response)
                        # print(f"Received {data}")
                        response_json = req()
                        conn.sendall(json.dumps(response_json).encode('UTF-8'))

    def response(self, message, status = 200):
        return { 'message': message, 'status': status, 'signature': serialize(keys.sign(message, self.private_key)) }

def local_server_factory(public_key, private_key, symmetric_key):
    return Server("127.0.0.1", 5121, public_key, private_key, symmetric_key)
