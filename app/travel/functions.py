from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.model import models
from . import schemas

def get_travel_by_id(db: Session, travel_id: int):
    return db.query(models.Travel).filter(models.Travel.id == travel_id).first()

def create_travel(db: Session, travel: schemas.TravelCreate):
    db_travel = models.Travel(
        travel_id=travel.travel_id,
        travel_date=travel.travel_date,
        total_cost=travel.total_cost,
        total_distance=travel.total_distance,
        user_id=travel.user_id,
        vehicle_plate=travel.vehicle_plate,
        fuel_id=travel.fuel_id
    )
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel
    
def update_travel(db: Session, travel_id: int, travel_update: schemas.TravelUpdate):
    db_travel = db.query(models.Travel).filter(models.Travel.travel_id == travel_id).first()

    if not db_travel:
        return None

    if travel_update.travel_date is not None:
        db_travel.travel_date = travel_update.travel_date
    if travel_update.total_cost is not None:
        db_travel.total_cost = travel_update.total_cost
    if travel_update.total_distance is not None:
        db_travel.total_distance = travel_update.total_distance
    if travel_update.vehicle_plate is not None:
        db_travel.vehicle_plate = travel_update.vehicle_plate
    if travel_update.fuel_id is not None:
        db_travel.fuel_id = travel_update.fuel_id

    db.commit()
    db.refresh(db_travel)
    return db_travel

def delete_travel(db: Session, travel_id: int):
    db_travel = db.query(models.Travel).filter(models.Travel.travel_id == travel_id).first()

    if not db_travel:
        return None

    db.delete(db_travel)
    db.commit()
    return db_travel

def get_travels(db: Session):
    return db.query(models.Travel).all()