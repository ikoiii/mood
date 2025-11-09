from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.patient import Patient

router = APIRouter()

@router.get("/patient/{token}")
async def authenticate_patient(token: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.qr_token == token).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Invalid QR token")
    return patient

@router.post("/admin/login")
async def admin_login():
    # TODO: Implement admin login with JWT
    return {"message": "Admin login endpoint - to be implemented"}