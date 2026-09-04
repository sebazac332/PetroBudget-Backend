from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.model import models
from app.dependencies import utils
from . import schemas

def get_vehicle_by_plate(db: Session, plate_number: str):
    return db.query(models.Vehicle).filter(models.Vehicle.plate_number == plate_number).first()

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(
        plate_number=vehicle.plate_number,
        manufacturer=vehicle.manufacturer,
        model=vehicle.model,
        engine=vehicle.engine,
        fuel_type=vehicle.fuel_type,
        tank_capacity=vehicle.tank_capacity,
        avg_fuel_consumption=vehicle.avg_fuel_consumption,
        wheel_number=vehicle.wheel_number,
        user_id=vehicle.user_id
    )
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def update_vehicle(db: Session, plate_number: str, vehicle_update: schemas.VehicleUpdate):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.plate_number == plate_number).first()

    if not db_vehicle:
        return None

    if vehicle_update.manufacturer is not None:
        db_vehicle.manufacturer = vehicle_update.manufacturer
    if vehicle_update.model is not None:
        db_vehicle.model = vehicle_update.model
    if vehicle_update.engine is not None:
        db_vehicle.engine = vehicle_update.engine
    if vehicle_update.fuel_type is not None:
        db_vehicle.fuel_type = vehicle_update.fuel_type
    if vehicle_update.tank_capacity is not None:
        db_vehicle.tank_capacity = vehicle_update.tank_capacity
    if vehicle_update.avg_fuel_consumption is not None:
        db_vehicle.avg_fuel_consumption = vehicle_update.avg_fuel_consumption
    if vehicle_update.wheel_number is not None:
        db_vehicle.wheel_number = vehicle_update.wheel_number

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, plate_number: str):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.plate_number == plate_number).first()

    if not db_vehicle:
        return None 

    db.delete(db_vehicle)
    db.commit()
    return db_vehicle

def get_vehicles(db: Session):
    return db.query(models.Vehicle).all()