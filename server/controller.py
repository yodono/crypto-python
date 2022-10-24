from pytz import UTC
import keys
import rsa

class Controller:
    def __init__(self, server):
        self.server = server

    def public_key(self):
        with open('server/keys/publicKey.pem', 'rb') as p:
            return p.read()

    def auth(self, body):
        print(type(body))
        # with open('server/keys/privateKey.pem', 'rb') as p:
        #     private_key = rsa.PrivateKey.load_pkcs1(p.read())

        #     print(rsa.decrypt(body.encode('UTF-8'), private_key))
        # print(keys.decrypt(body, self.server.private_key))
        return "OK".encode('UTF-8')
