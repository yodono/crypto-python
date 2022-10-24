import rsa

def generate_keys():
    (public_key, private_key) = rsa.newkeys(1024)
    with open('server/keys/publicKey.pem', 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))
    with open('server/keys/privateKey.pem', 'wb') as p:
        p.write(private_key.save_pkcs1('PEM'))

def load_keys():
    with open('server/keys/publicKey.pem', 'rb') as p:
        public_key = rsa.PublicKey.load_pkcs1(p.read())
    with open('server/keys/privateKey.pem', 'rb') as p:
        private_key = rsa.PrivateKey.load_pkcs1(p.read())
    return private_key, public_key

def decrypt(ciphertext, private_key):
    try:
        return rsa.decrypt(ciphertext, private_key).decode('UTF-8')
    except:
        return False

def sign(msg, private_key):
    return rsa.sign(msg.encode('UTF-8'), private_key, 'SHA-1')
