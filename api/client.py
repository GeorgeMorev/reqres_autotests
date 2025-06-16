import requests


class ReqresClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

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
