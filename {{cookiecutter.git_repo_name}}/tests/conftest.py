import os, sys
import pytest
from fastapi.testclient import TestClient
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))
from modules.web_app import web_app


@pytest.fixture
def fastapi_mock_client():
    yield TestClient(web_app)
