import base64

def serialize(bytes):
    return base64.b64encode(bytes).decode()

def deserialize(string):
    return base64.b64decode(string.encode())
