from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    mood = Column(String(50), nullable=False)
    pain_level = Column(Integer, nullable=False)  # 0-10 scale
    note = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship with Patient
    patient = relationship("Patient", back_populates="entries")

    def __repr__(self):
        return f"<Entry(id={self.id}, patient_id={self.patient_id}, mood='{self.mood}', pain_level={self.pain_level})>"