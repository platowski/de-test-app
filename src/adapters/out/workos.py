from fastapi import Depends

from utils.workos_client import get_client


class WorkOsAdapter:
    def __init__(self, client=Depends(get_client)):
        self.client = client

    def get_users(self):
        return self.client.user_management.list_users()
