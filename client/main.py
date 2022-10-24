import json
from src import client, service, keys
from src.utils.serialize import serialize
from src.utils import colors

if __name__ == "__main__":
    _client = client.local_client_factory()
    _service = service.Service(_client.send)

    # Load key
    public_key = keys.load_key(_service.get("/public_key"))

    # Auth
    name = input("Digite seu nome: ")
    pwd = input("Digite sua senha: ")

    ciphered_name = keys.encrypt(name, public_key)
    ciphered_pwd = keys.encrypt(pwd, public_key)
    auth_response = _service.post("/auth", json.dumps({
        'name': serialize(ciphered_name),
        'pwd': serialize(ciphered_pwd)
    }))

    print(colors.wrap('purple', auth_response))
