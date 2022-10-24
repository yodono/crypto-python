import client
import service
import keys

_client = client.local_client_factory()
_service = service.Service(_client.send)

public_key = _service.get("/public_key")
cypertext = keys.encrypt('it worked!', keys.load_key(public_key))

response = _service.post("/auth", keys.serialize(cypertext))
print(response)

# name = input("Digite seu nome: ")
# pwd = input("Digite sua senha: ")

# _service.post("auth", f"{name},{pwd}")
