from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/", response_model=schemas.Vehicle)
def register_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    if functions.get_vehicle_by_plate(db, vehicle.plate_number):
        raise HTTPException(status_code=400, detail="A vehicle with this plate number already exists.")
    return functions.create_vehicle(db, vehicle)

@router.put("/{plate_number}", response_model=schemas.Vehicle)
def edit_vehicle(plate_number: str, vehicle_update: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    vehicle = functions.update_vehicle(db, plate_number, vehicle_update)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{plate_number}", response_model=schemas.Vehicle)
def remove_vehicle(plate_number: str, db: Session = Depends(get_db)):
    vehicle = functions.delete_vehicle(db, plate_number)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle