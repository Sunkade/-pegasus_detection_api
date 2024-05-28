import shutil
from fastapi import HTTPException, Header
import jwt

SECRET_KEY = "your_secret_key"  # Replace with a secure secret key

def save_upload_file(upload_file):
    file_location = f"/tmp/{upload_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(upload_file.file, file_object)
    return file_location

def validate_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
