from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.entry import Entry

router = APIRouter()

@router.get("/")
async def get_entries(db: Session = Depends(get_db)):
    entries = db.query(Entry).all()
    return entries

@router.post("/")
async def create_entry():
    # TODO: Implement entry creation
    return {"message": "Entry creation endpoint - to be implemented"}

@router.get("/{entry_id}")
async def get_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter(Entry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry