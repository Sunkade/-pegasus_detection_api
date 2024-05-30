from fastapi.testclient import TestClient
from app.main import app
import jwt

client = TestClient(app)
SECRET_KEY = "your_secret_key"

def get_token():
    payload = {"sub": "test"}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return f"Bearer {token}"

def test_memory_forensics():
    token = get_token()
    with open("tests/sample_memory_dump.raw", "rb") as memory_dump:
        response = client.post("/memory/analyze", files={"memory_dump": memory_dump}, headers={"Authorization": token})
    assert response.status_code == 200
    assert "results" in response.json()
