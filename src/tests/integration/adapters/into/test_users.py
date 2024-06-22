import pytest


class TestUsersAdapter:

    @pytest.mark.asyncio
    async def test_get_users_returns_response(self, async_client):
        async with async_client as ac:
            response = await ac.get("/users")
            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_get_users_returns_empty_response_for_non_existing_before(
        self, async_client
    ):
        async with async_client as ac:
            response = await ac.get("/users?before=nonexistingid")
            assert response.status_code == 200
            response_json = response.json()
            assert response_json["users"] == []

    @pytest.mark.asyncio
    async def test_get_users_returns_unprocessable_status_on_input_validation_error(
        self, async_client
    ):
        async with async_client as ac:
            response = await ac.get("/users?limit=200")
            assert response.status_code == 422

            response = await ac.get("/users?before=sameid&after=sameid")
            assert response.status_code == 422
