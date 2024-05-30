import pytest
from fastapi.testclient import TestClient
from app.main import app
import jwt
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

SECRET_KEY = os.getenv("SECRET_KEY")  # Use environment variable

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def get_token():
    # Generate a valid JWT token
    payload = {"sub": "test"}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return f"Bearer {token}"
