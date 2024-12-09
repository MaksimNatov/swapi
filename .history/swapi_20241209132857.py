import requests

class APIRequester(url):

    def __init__(self, url):
        self.base_url = url

    def get_request(self):