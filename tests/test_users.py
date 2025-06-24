from api.client import ReqresClient
from api.endpoints import ENDPOINTS_DICTIONARY


def test_get_list_users(client):
    response = client.get(ENDPOINTS_DICTIONARY["list_users"])
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
