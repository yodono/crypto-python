import rsa

def load_key(public_key):
    return rsa.PublicKey.load_pkcs1(public_key)

def encrypt(msg, public_key):
    return rsa.encrypt(msg.encode('UTF-8'), public_key)

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False
