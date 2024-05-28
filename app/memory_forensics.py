from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import subprocess
from app.utils import save_upload_file, validate_token

router = APIRouter()

@router.post("/analyze", dependencies=[Depends(validate_token)])
def analyze_memory(memory_dump: UploadFile = File(...)):
    try:
        file_location = save_upload_file(memory_dump)
        results = subprocess.run(
            ["volatility", "-f", file_location, "--profile=WinXPSP2x86", "pslist"],
            capture_output=True, text=True
        )
        return {"status": "success", "results": results.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
