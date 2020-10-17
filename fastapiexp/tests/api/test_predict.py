from io import BytesIO

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


def test_predict_classification(fastapi_test_client: TestClient):
    """
    Predict classification
    """
    response = fastapi_test_client.post(
        "/api/predict/classification",
        files={"file": ("test.txt", BytesIO(b"This is test contents."))},
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_predict_classification_with_async(async_test_client: AsyncClient):
    """
    Predict classification
    """
    async with async_test_client as ac:
        response = await ac.post(
            "/api/predict/classification",
            files={"file": ("test.txt", BytesIO(b"This is test contents."))},
        )
    assert response.status_code == 200
