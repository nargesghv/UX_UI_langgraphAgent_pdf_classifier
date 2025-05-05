from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
from backend.agent_runner import classify_document

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save to /incoming
    incoming_dir = Path("incoming")
    incoming_dir.mkdir(exist_ok=True)
    file_path = incoming_dir / file.filename
    with file_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    # Classify using LangGraph
    try:
        result = classify_document(str(file_path))
        return JSONResponse({"filename": file.filename, "classification": result})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
