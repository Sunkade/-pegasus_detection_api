from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import subprocess
from app.utils import save_upload_file, validate_token

router = APIRouter()

@router.post("/analyze", dependencies=[Depends(validate_token)])
def analyze_mobile_device(mobile_data: UploadFile = File(...)):
    try:
        file_location = save_upload_file(mobile_data)
        results = subprocess.run(
            ["mvt-ios", "check-backup", file_location],
            capture_output=True, text=True
        )
        return {"status": "success", "results": results.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
