import json
from src import client, service, keys
from src.utils.serialize import serialize, deserialize

if __name__ == "__main__":
    _client = client.local_client_factory()
    _service = service.Service(_client.send)

    # Load key
    public_key_response = _service.get("/public_key")
    public_key = keys.load_key(deserialize(public_key_response['message']))

    # Auth
    name = input("Digite seu nome: ")
    pwd = input("Digite sua senha: ")

    ciphered_name = keys.encrypt(name, public_key)
    ciphered_pwd = keys.encrypt(pwd, public_key)
    auth_response = _service.post("/auth", json.dumps({
        'name': serialize(ciphered_name),
        'pwd': serialize(ciphered_pwd)
    }))

    _client.handle_response(auth_response)
