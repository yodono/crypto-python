import client
import service
import keys
import rsa

_client = client.local_client_factory()
_service = service.Service(_client.send)

public_key = _service.get("/public_key")
cypertext = keys.encrypt('bundinha', keys.load_key(public_key))

with open('server/keys/privateKey.pem', 'rb') as p:
    private_key = rsa.PrivateKey.load_pkcs1(p.read())

    print(rsa.decrypt(cypertext, private_key))

response = _service.post("/auth", cypertext)
# print(response)

# name = input("Digite seu nome: ")
# pwd = input("Digite sua senha: ")

# _service.post("auth", f"{name},{pwd}")
