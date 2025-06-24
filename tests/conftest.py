import pytest
from api.client import ReqresClient


@pytest.fixture(scope="session")
def client():
    return ReqresClient()
