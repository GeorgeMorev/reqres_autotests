from enum import Enum
from urllib.parse import urlencode

BASE_URL = "https://reqres.in/api"


class Endpoints(Enum):
    LIST_USERS = "/users"
    SINGLE_USER = "/users/{id}"
    LOGIN = "/login"
    REGISTER = "/register"

    def url_with_params(self, params: dict | None = None) -> str:
        base = self.value
        if params:
            return f"{base}?{urlencode(params)}"
        return base
