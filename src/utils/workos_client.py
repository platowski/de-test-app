import workos
from utils.env import env_settings

workos.client_id = env_settings.workos_client_id
workos.api_key = env_settings.workos_api_key


# Dependency
def get_client():
    return workos.client
