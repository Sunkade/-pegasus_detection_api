from fastapi import UploadFile
def test_file_system_analysis(client, get_token):
    token = get_token
    with open("tests/sample_disk_image.dd", "rb") as disk_image:
        files = {"disk_image": UploadFile(disk_image)}
        response = client.post("/file/analyze", files=files, headers={"Authorization": token})

    assert response.status_code == 200
    assert response.json()["status"] == "success"
