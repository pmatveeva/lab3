from Base import BaseClient
import requests
import json


class Client(BaseClient):
    BASE_URL = 'https://api.vk.com/method/users.get'
    http_method = 'GET'

    def __init__(self, name):
        self.name = name

    def get_params(self):
        return 'user_ids=' + self.name

    def response_handler(self, response):
        try:
            return json.loads(response.text).get('response')[0].get('uid')
        except:
            raise Exception("Запрос не может быть обработан")

    def _get_data(self, method, http_method):
        response = None

        response = requests.get(self.BASE_URL + '?' + self.get_params())
        return self.response_handler(response)