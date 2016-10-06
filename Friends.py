from Base import BaseClient
import requests
import json
from datetime import datetime


class Friends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/friends.get'
    http_method = 'GET'

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return 'user_id=' + str(self.user_id) + '&fields=bdate'

    def response_handler(self, response):
        try:
            friends = json.loads(response.text).get('response')

            ages = []

            for friend in friends:
                birth_date = friend.get('bdate')

                if birth_date is None or len(birth_date) < 8:
                    continue

                birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
                cur_date = datetime.now()

                ages.append(int((cur_date - birth_date).days) // 365.2425)

            ages_ =list(set(ages))
            return sorted([(x, ages.count(x)) for x in ages_])
        except:
            raise Exception("Запрос не может быть обработан")

    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL + '?' + self.get_params())
        return self.response_handler(response)