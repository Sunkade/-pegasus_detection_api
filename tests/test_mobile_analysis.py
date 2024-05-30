from fastapi.testclient import TestClient
from app.main import app
import jwt

client = TestClient(app)
SECRET_KEY = "your_secret_key"

def get_token():
    payload = {"sub": "test"}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return f"Bearer {token}"

def test_mobile_analysis():
    token = get_token()
    with open("tests/sample_mobile_data.zip", "rb") as mobile_data:
        response = client.post("/mobile/analyze", files={"mobile_data": mobile_data}, headers={"Authorization": token})
    assert response.status_code == 200
    assert "results" in response.json()
