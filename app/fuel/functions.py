from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.model import models
from app.dependencies import utils
from . import schemas

def get_fuel_by_id(db: Session, fuel_id: int):
    return db.query(models.Fuel).filter(models.Fuel.fuel_id == fuel_id).first()

def create_fuel(db: Session, fuel: schemas.FuelCreate):
    db_fuel = models.Fuel(
        fuel_type=fuel.fuel_type,
        price_per_gallon=fuel.price_per_gallon,
        fuel_station=fuel.fuel_station,
        user_id=fuel.user_id
    )
    db.add(db_fuel)
    db.commit()
    db.refresh(db_fuel)
    return db_fuel

def update_fuel(db: Session, fuel_id: int, fuel_update: schemas.FuelUpdate):
    db_fuel = db.query(models.Fuel).filter(models.Fuel.fuel_id == fuel_id).first()

    if not db_fuel:
        return None

    if fuel_update.fuel_type is not None:
        db_fuel.fuel_type = fuel_update.fuel_type
    if fuel_update.price_per_gallon is not None:
        db_fuel.price_per_gallon = fuel_update.price_per_gallon
    if fuel_update.fuel_station is not None:
        db_fuel.fuel_station = fuel_update.fuel_station

    db.commit()
    db.refresh(db_fuel)
    return db_fuel

def get_fuels(db: Session):
    return db.query(models.Fuel).all()