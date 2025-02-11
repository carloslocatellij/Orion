import pytest
from fastapi.testclient import TestClient

from orion.app import app


@pytest.fixture
def client():
    return TestClient(app)
