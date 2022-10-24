import json

class Service:
    def __init__(self, send):
        self.send = send

    def get(self, endpoint = "", body = ""):
        return self.send(json.dumps({ 'method': 'get', 'endpoint': endpoint, 'body': body }))
    
    def post(self, endpoint = "", body = ""):
        return self.send(json.dumps({ 'method': 'post', 'endpoint': endpoint, 'body': body }))
