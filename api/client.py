import requests
from api.endpoints import BASE_URL
from api.endpoints import ENDPOINTS_DICTIONARY


class ReqresClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": "reqres-free-v1"
        })

    def post(self, endpoint, data=None, json=None, **kwargs):
        url = self.base_url + endpoint
        return self.session.post(url, data=data, json=json, **kwargs)

    def get(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        return self.session.get(url, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        url = self.base_url + endpoint
        return self.session.put(url, data=data, json=json, **kwargs)

    def patch(self, endpoint, data=None, json=None, **kwargs):
        url = self.base_url + endpoint
        return self.session.patch(url, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        return self.session.delete(url, **kwargs)

    def get_users_list(self):
        return self.get(ENDPOINTS_DICTIONARY["list_users"])
