from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models

router = APIRouter(prefix="/travels", tags=["Travels"])

@router.post("/", response_model=schemas.Travel)
def register_travel(travel: schemas.TravelCreate, db: Session = Depends(get_db)):
    if functions.get_travel_by_id(db, travel.travel_id):
        raise HTTPException(status_code=400, detail="A travel with this ID already exists.")
    return functions.create_travel(db, travel)

@router.put("/{travel_id}", response_model=schemas.Travel)
def edit_travel(travel_id: int, travel_update: schemas.TravelUpdate, db: Session = Depends(get_db)):
    travel = functions.update_travel(db, travel_id, travel_update)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel

@router.delete("/{travel_id}", response_model=schemas.Travel)
def remove_travel(travel_id: int, db: Session = Depends(get_db)):
    travel = functions.delete_travel(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel