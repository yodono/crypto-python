import json
from . import symmetric, keys
from .utils.serialize import serialize

def user_factory(name, pwd):
    return {
        'name': name,
        'pwd': pwd
    }

# TODO: add way to add users to whitelist
WHITELIST_PATH = 'server/secret/whitelist.json'
WHITELIST = [
    user_factory('victor yodono', 'unipvy123'),
    user_factory('gustavo cabral correia', 'unipgcc123'),
    user_factory('guilherme brito pinheiro', 'unipgbp123'),
    user_factory('leonardo basilio diniz', 'uniplbd123'),
    user_factory('lucas henrique masson', 'uniplhm123')
]

def encrypt(key):
    for user in WHITELIST:
        user['name'] = serialize(symmetric.encrypt(user['name'].encode(), key))
        user['pwd'] = hash(user['pwd'])

    with open(WHITELIST_PATH, 'w') as f:
        f.write(json.dumps(WHITELIST))
