from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing CORS for all origins, adjust as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .network_analysis import router as network_router
from .memory_forensics import router as memory_router
from .file_system_analysis import router as file_router
from .mobile_analysis import router as mobile_router

app.include_router(network_router, prefix="/network")
app.include_router(memory_router, prefix="/memory")
app.include_router(file_router, prefix="/file")
app.include_router(mobile_router, prefix="/mobile")
