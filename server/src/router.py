import json

class Router:
    def __init__(self):
        self.methods = {
            "get": {},
            "post": {},
        }
    
    def parse(self, request):
        data = json.loads(request)
        method = data['method']
        endpoint = data['endpoint']
        body = data['body']

        if method not in self.methods:
            return lambda: "405: Method not allowed"

        if endpoint not in self.methods[method]:
            return lambda: "404: Not found"

        if not body:
            return lambda: self.methods[method][endpoint]()

        return lambda: self.methods[method][endpoint](body)

    def get(self, endpoint, callback):
        self.methods['get'][endpoint] = callback

    def post(self, endpoint, callback):
        self.methods['post'][endpoint] = callback
