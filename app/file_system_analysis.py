from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import subprocess
from app.utils import save_upload_file, validate_token

router = APIRouter()

@router.post("/analyze", dependencies=[Depends(validate_token)])
def analyze_file_system(disk_image: UploadFile = File(...)):
    try:
        file_location = save_upload_file(disk_image)
        results = subprocess.run(
            ["tsk_recover", file_location, "/tmp/recover_dir"],
            capture_output=True, text=True
        )
        return {"status": "success", "results": results.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
