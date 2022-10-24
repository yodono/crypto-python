import client
import service
import keys
import json

_client = client.local_client_factory()
_service = service.Service(_client.send)

public_key = keys.load_key(_service.get("/public_key"))

name = input("Digite seu nome: ")
pwd = input("Digite sua senha: ")

ciphered_name = keys.encrypt(name, public_key)
ciphered_pwd = keys.encrypt(pwd, public_key)
auth_response = _service.post("/auth", json.dumps({
    'name': keys.serialize(ciphered_name),
    'pwd': keys.serialize(ciphered_pwd)
}))

print(auth_response)
