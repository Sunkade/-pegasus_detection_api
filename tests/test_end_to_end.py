from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_analyze_network():
    response = client.post(
        "/network/analyze",
        json={"filter": "tcp", "count": 10},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()

def test_analyze_memory():
    with open("tests/sample_memory_dump.dmp", "rb") as file:
        response = client.post(
            "/memory/analyze",
            files={"memory_dump": file},
        )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()

def test_analyze_file_system():
    with open("tests/sample_disk_image.img", "rb") as file:
        response = client.post(
            "/file/analyze",
            files={"disk_image": file},
        )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()

def test_analyze_mobile_device():
    with open("tests/sample_mobile_data.zip", "rb") as file:
        response = client.post(
            "/mobile/analyze",
            files={"mobile_data": file},
        )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()
