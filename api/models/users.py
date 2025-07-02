from pydantic import BaseModel, HttpUrl


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class ListUsersResponse(BaseModel):
    data: list[User]
