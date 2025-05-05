from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ClassificationRecord(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    classification = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
