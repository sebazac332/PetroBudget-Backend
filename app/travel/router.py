from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models

router = APIRouter(prefix="/travels", tags=["Travels"])

@router.post("/", response_model=schemas.Travel)
def register_travel(travel: schemas.TravelCreate, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.plate_number == travel.vehicle_plate).first()
    fuel = db.query(models.Fuel).filter(models.Fuel.fuel_id == travel.fuel_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    if vehicle.user_id != travel.user_id:
        raise HTTPException(status_code=403, detail="The vehicle does not belong to the user")
    
    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel not found")

    if fuel.user_id != travel.user_id:
        raise HTTPException(status_code=403, detail="The fuel does not belong to the user")

    if fuel.fuel_type != vehicle.fuel_type:
        raise HTTPException(status_code=400, detail="The fuel type does not match the vehicle's fuel type, the vehicle uses " + vehicle.fuel_type.value)

    return functions.create_travel(db, travel)

@router.put("/{travel_id}", response_model=schemas.Travel)
def edit_travel(travel_id: int, travel_update: schemas.TravelUpdate, db: Session = Depends(get_db)):
    travel = functions.update_travel(db, travel_id, travel_update)

    vehicle = db.query(models.Vehicle).filter(models.Vehicle.plate_number == travel.vehicle_plate).first()
    fuel = db.query(models.Fuel).filter(models.Fuel.fuel_id == travel.fuel_id).first()

    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    if vehicle.user_id != travel.user_id:
        raise HTTPException(status_code=403, detail="The vehicle does not belong to the user")
    
    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel not found")

    if fuel.user_id != travel.user_id:
        raise HTTPException(status_code=403, detail="The fuel does not belong to the user")

    if fuel.fuel_type != vehicle.fuel_type:
        raise HTTPException(status_code=400, detail="The fuel type does not match the vehicle's fuel type, the vehicle uses " + vehicle.fuel_type.value)

    return travel

@router.delete("/{travel_id}", response_model=schemas.Travel)
def remove_travel(travel_id: int, db: Session = Depends(get_db)):
    travel = functions.delete_travel(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel