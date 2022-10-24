from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open('server/keys/symmetric.key', 'wb') as p:
        p.write(key)

def load_key():
    with open('server/keys/symmetric.key', 'rb') as p:
        return Fernet(p.read())

def encrypt(data, key):
    return key.encrypt(data)

def decrypt(data, key):
    return key.decrypt(data).decode()
