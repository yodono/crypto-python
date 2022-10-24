import json
from . import keys, symmetric
from .utils.serialize import deserialize 

class Controller:
    def __init__(self, server):
        self.server = server

    def public_key(self):
        with open('server/keys/publicKey.pem', 'rb') as p:
            return p.read()

    def auth(self, body):
        parsed = json.loads(body)
        name = deserialize(parsed['name'])
        pwd = deserialize(parsed['pwd'])

        deciphered_name = keys.decrypt(name, self.server.private_key)
        deciphered_pwd = keys.decrypt(pwd, self.server.private_key)

        with open('server/secret/whitelist.json', 'r') as f:
            whitelist_json = json.loads(f.read()) # TODO: handle empty file exception

        for user in whitelist_json:
            target_pwd = user['pwd']
            target_name = symmetric.decrypt(deserialize(user['name']), self.server.symmetric_key)

            if target_pwd == hash(deciphered_pwd) and target_name == deciphered_name.lower():
                return "Acesso liberado.".encode('UTF-8')

        return "Acesso negado. Senha ou usuário inválidos.".encode('UTF-8')
