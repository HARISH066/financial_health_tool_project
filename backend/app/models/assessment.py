from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base
from datetime import datetime

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, nullable=False)
    risk = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
