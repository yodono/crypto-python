import keys

class Controller:
    def __init__(self, server):
        self.server = server

    def public_key(self):
        with open('server/keys/publicKey.pem', 'rb') as p:
            return p.read()

    def auth(self, body):
        cypertext = keys.deserialize(body)
        # print(keys.decrypt(cypertext, self.server.private_key))
        return "OK".encode('UTF-8')
