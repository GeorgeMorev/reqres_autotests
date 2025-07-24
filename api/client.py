import requests
from api.endpoints import BASE_URL, Endpoints


class ReqresClient:
    def __init__(self, token: str | None = "reqres-free-v1"):
        self.base_url = BASE_URL
        self.session = requests.Session()
        if token:
            self.session.headers.update({"x-api-key": token})

    def _make_url(self, endpoint: Endpoints) -> str:
        return self.base_url + endpoint.value

    def post(self, endpoint, data=None, json=None, **kwargs):
        url = self._make_url(endpoint)
        return self.session.post(url, data=data, json=json, **kwargs)

    def get(self, endpoint: Endpoints, **kwargs):
        url = self._make_url(endpoint)
        return self.session.get(url, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        url = self._make_url(endpoint)
        return self.session.put(url, data=data, json=json, **kwargs)

    def patch(self, endpoint, data=None, json=None, **kwargs):
        url = self._make_url(endpoint)
        return self.session.patch(url, data=data, json=json, **kwargs)

    # Функция для отправки запроса delete
    # Принимаемый аргумент - URL для отправки запроса
    def delete(self, endpoint, **kwargs):
        url = self._make_url(endpoint)
        return self.session.delete(url, **kwargs)

    def get_users_list(self):
        return self.get(Endpoints.LIST_USERS)
