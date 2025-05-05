from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

from backend.agent_runner import classify_document
from backend.db.database import SessionLocal
from backend.db.crud import get_all_records, create_record

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    incoming_dir = Path("incoming")
    incoming_dir.mkdir(exist_ok=True)
    file_path = incoming_dir / file.filename
    with file_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        result = classify_document(str(file_path))
        # Save to DB
        db = SessionLocal()
        create_record(db, file.filename, result)
        return JSONResponse({"filename": file.filename, "classification": result})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@router.get("/history")
def get_classification_history():
    db = SessionLocal()
    records = get_all_records(db)
    return [
        {
            "filename": r.filename,
            "classification": r.classification,
            "timestamp": r.timestamp.isoformat()
        }
        for r in records
    ]

