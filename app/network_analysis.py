from fastapi import APIRouter, HTTPException, Depends
import scapy.all as scapy
from pydantic import BaseModel
from typing import List
from app.utils import validate_token

router = APIRouter()

class NetworkAnalysisRequest(BaseModel):
    filter: str
    count: int

class NetworkAnalysisResponse(BaseModel):
    status: str
    results: List[dict]

@router.post("/analyze", response_model=NetworkAnalysisResponse, dependencies=[Depends(validate_token)])
def analyze_network(request: NetworkAnalysisRequest):
    try:
        packets = scapy.sniff(filter=request.filter, count=request.count, timeout=10)
        results = [{"summary": packet.summary()} for packet in packets]
        return {"status": "success", "results": results}
    except scapy.Scapy_Exception as e:
        raise HTTPException(status_code=500, detail=f"Scapy error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
