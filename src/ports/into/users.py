from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]


class GetUsersPageDTO(BaseModel):
    before: Optional[str]
    after: Optional[str]
    email: Optional[str]
    page_size: Optional[int]


class UsersPageDTO(BaseModel):
    users: list[UserDTO]
    before: Optional[str]
    after: Optional[str]
