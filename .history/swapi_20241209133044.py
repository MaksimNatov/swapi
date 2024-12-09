import requests

class APIRequester(url):

    def __init__(self, url):
        self.base_url = url

    def get_request(self):
        try
        return requests.get(self.base_url)