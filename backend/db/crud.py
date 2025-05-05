from .models import ClassificationRecord
from sqlalchemy.orm import Session

def create_record(db: Session, filename: str, classification: str):
    record = ClassificationRecord(filename=filename, classification=classification)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all_records(db: Session):
    return db.query(ClassificationRecord).order_by(ClassificationRecord.timestamp.desc()).all()
