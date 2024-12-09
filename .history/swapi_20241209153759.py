import requests
from pathlib import Path

class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint = ''):
        try:
            self.response = requests.get(f'{self.base_url}{endpoint}')
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
        
        response = requests.get(sw_type )
        return response.text

    def save_sw_data():
        sw_req = SWRequester()
        Path('./data/').mkdir(parents=True, exist_ok=True)
        category = sw_req.get_sw_categories()
        for i in category:
            text = sw_req.get_sw_info(i)
            with open(f'./data/{i}.txt', 'w') as f:
                f.write(text)

save_sw_data()