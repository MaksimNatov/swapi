import requests
import pathlib

class APIRequester:

    def __init__(self, url):
        self.base_url = url

    def get_request(self):
        try:
            self.response = requests.get(self.base_url)
            self.response.raise_for_status()
            return self.response
        except requests.exceptions.RequestException as e:
            return  print(e)

class SWRequester(APIRequester):

    def get_sw_categories(self):
        self.response = requests.get('https://swapi.dev/api/')
        return list(self.response.json().keys())
    
    #sw_type = list(self.response.json().keys())[0]

    def get_sw_info(self, sw_type):
        
        self.response = requests.get(f'https://swapi.dev/api/{sw_type}/')
        return self.response.text

    def save_sw_data(self):
        Path()
        category = self.get_sw_categories()
        for i in category:
            text = self.get_sw_info(i)

a = SWRequester('https://swapi.dev/')
print(a.get_request().__class__)
print(a.get_request().status_code)
print(a.get_sw_categories())
print(a.get_sw_info('people'))
