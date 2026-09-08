from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models
    
router = APIRouter(prefix="/fuels", tags=["Fuels"])

@router.post("/", response_model=schemas.Fuel)
def register_fuel(fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    if functions.get_fuel_by_id(db, fuel.fuel_id):
        raise HTTPException(status_code=400, detail="A fuel with this ID already exists.")
    return functions.create_fuel(db, fuel)

@router.put("/{fuel_id}", response_model=schemas.Fuel)
def edit_fuel(fuel_id: int, fuel_update: schemas.FuelUpdate, db: Session = Depends(get_db)):
    fuel = functions.update_fuel(db, fuel_id, fuel_update)
    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel not found")
    return fuel

@router.delete("/{fuel_id}", response_model=schemas.Fuel)
def remove_fuel(fuel_id: int, db: Session = Depends(get_db)):
    fuel = functions.delete_fuel(db, fuel_id)
    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel not found")
    return fuel