import json

class Service:
    def __init__(self, send):
        self.send = send

    def get(self, endpoint = "", body = ""):
        return self.send(f"get::{endpoint}::{body}")
    
    def post(self, endpoint = "", body = ""):
        return self.send(f"post::{endpoint}::{body}")
