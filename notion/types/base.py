import requests

class Base:
    def __init__(self, token):
        self.token = token
        self.headers = {