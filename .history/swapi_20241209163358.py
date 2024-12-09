import os
from pathlib import Path


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()  # Проверка статуса
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")


class SWRequester(APIRequester):
    def __init__(self):
        super().__init__("https://swapi.dev/api/")

    def get_sw_categories(self):
        response = self.get()
        if response:
            return list(response.json().keys())  # Возврат доступных категорий

    def get_sw_info(self, sw_type):
        response = self.get(sw_type + '/')
        if response:
            print(response.text)
            return response.text  # Возврат ответа в виде строки


def save_sw_data():
    sw_requester = SWRequester()

    # Создание директории для сохранения данных
    Path("/data/").mkdir(parents=True, exist_ok=True) 

    # Получение списка категорий
    categories = sw_requester.get_sw_categories()

    # Запись данных в файлы
    for category in categories:
        info = sw_requester.get_sw_info(category)

        if info:

            with open(f"data/{category}.txt", 'w') as file:
                file.write(info)

# Вызов функции для сохранения данных


save_sw_data()
