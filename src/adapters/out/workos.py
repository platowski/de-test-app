from fastapi import Depends

from ports.into.users import UserDTO, UsersPageDTO, GetUsersPageDTO
from utils.workos_client import get_client


class WorkOsAdapter:
    def __init__(self, client=Depends(get_client)):
        self.client = client

    def get_users(self, dto: GetUsersPageDTO) -> UsersPageDTO:
        # no try, let it fail. At least until it becomes a problem
        users_response = self.client.user_management.list_users(
            limit=dto.page_size, before=dto.before, after=dto.after, email=dto.email
        )
        return UsersPageDTO(
            before=users_response.list_metadata["before"],
            after=users_response.list_metadata["after"],
            users=[UserDTO(**user) for user in users_response.data],
        )
