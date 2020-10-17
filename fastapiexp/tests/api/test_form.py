import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from fastapiexp.api.routers.form import COOKIE_KEY
from fastapiexp.infrastructure.session.redis_store import client


def test_send_form(fastapi_test_client: TestClient):
    """
    Send form data
    """
    response = fastapi_test_client.post(
        "/form/send",
        data={
            "name": "test",
            "email": "test@example.com",
            "company": "test company",
        },
    )
    assert response.status_code == 204
    cookies = response.cookies
    cookie = cookies.get(COOKIE_KEY, domain="testserver.local", path="/predict")
    assert cookie
    stored_value = client.get(cookie)
    assert stored_value == b"session_id"
    client.delete(cookie)


@pytest.mark.asyncio
async def test_send_form_with_async(async_test_client: AsyncClient):
    """
    Send form data
    """
    async with async_test_client as ac:
        response = await ac.post(
            "/form/send",
            data={
                "name": "test",
                "email": "test@example.com",
                "company": "test company",
            },
        )
    assert response.status_code == 204
    cookies = response.cookies
    cookie = cookies.get(COOKIE_KEY)
    assert cookie
    stored_value = client.get(cookie)
    assert stored_value == b"session_id"
    client.delete(cookie)
