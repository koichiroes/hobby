import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from fastapiexp.api.app import create_app


@pytest.fixture(scope="session")
def fastapi_test_client() -> TestClient:
    app = create_app()
    return TestClient(app)


@pytest.fixture(scope="session")
def async_test_client():
    app = create_app()
    return AsyncClient(app=app, base_url="http://test")
