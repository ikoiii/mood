from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.patient import Patient

router = APIRouter()

@router.get("/")
async def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients

@router.post("/")
async def create_patient():
    # TODO: Implement patient creation
    return {"message": "Patient creation endpoint - to be implemented"}

@router.get("/{patient_id}")
async def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient