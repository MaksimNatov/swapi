import requests
from pathlib import Path

class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self):
        try:
            self.response = requests.get(self.base_url)
            self.response.raise_for_status()
            return self.response
        except requests.exceptions.RequestException as e:
            print(e)

class SWRequester(APIRequester):

    def __init__(self):
        super().__init__('https://swapi.dev/api/')

    def get_sw_categories(self):
        response = self.get()
        return list(response.json().keys())
    
    
    def get_sw_info(self, sw_type):
        
        response = requests.get(f'https://swapi.dev/api/{sw_type}/')
        return response.text

    def save_sw_data(self, sw_type):
       

a = SWRequester('https://swapi.dev/')
print(a.get_request().__class__)
print(a.get_request().status_code)
print(a.get_sw_categories())
print(a.get_sw_info('people'))
b.save_sw_data()