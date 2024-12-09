import requests

class APIRequester:

    def __init__(self, url):
        self.base_url = url

    def get_request(self):
        try:
            return requests.get(self.base_url)
        except requests.exceptions.RequestException as e:
            print(e)

class SWRequester(APIRequester):

    def get_sw_categories():
        response = 

a = APIRequester('https://swapi.dev/')
print(a.get_request().__class__)