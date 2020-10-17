import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


def test_index(fastapi_test_client: TestClient):
    """
    Get index.html
    """
    response = fastapi_test_client.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_index_with_async(async_test_client: AsyncClient):
    """
    Get index.html
    """
    async with async_test_client as ac:
        response = await ac.get("/")
    assert response.status_code == 200
