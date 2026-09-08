from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.model import models
from . import schemas

def get_travelpoint_by_id(db: Session, point_id: int):
    return db.query(models.Travelpoint).filter(models.Travelpoint.point_id == point_id).first()

def create_travelpoint(db: Session, travelpoint: schemas.TravelpointCreate):
    db_travelpoint = models.Travelpoint(
        point_name=travelpoint.point_name,
        distance_from_last_point=travelpoint.distance_from_last_point,
        last_point_id=travelpoint.last_point_id,
        travel_id=travelpoint.travel_id
    )
    db.add(db_travelpoint)
    db.commit()
    db.refresh(db_travelpoint)
    return db_travelpoint

def update_travelpoint(db: Session, point_id: int, travelpoint_update: schemas.TravelpointUpdate):
    db_travelpoint = db.query(models.Travelpoint).filter(models.Travelpoint.point_id == point_id).first()

    if not db_travelpoint:
        return None

    if travelpoint_update.point_name is not None:
        db_travelpoint.point_name = travelpoint_update.point_name
    if travelpoint_update.distance_from_last_point is not None:
        db_travelpoint.distance_from_last_point = travelpoint_update.distance_from_last_point
    if travelpoint_update.last_point_id is not None:
        db_travelpoint.last_point_id = travelpoint_update.last_point_id
    if travelpoint_update.travel_id is not None:
        db_travelpoint.travel_id = travelpoint_update.travel_id

    db.commit()
    db.refresh(db_travelpoint)
    return db_travelpoint

def delete_travelpoint(db: Session, point_id: int):
    db_travelpoint = db.query(models.Travelpoint).filter(models.Travelpoint.point_id == point_id).first()

    if not db_travelpoint:
        return None

    db.delete(db_travelpoint)
    db.commit()
    return db_travelpoint

def get_travelpoints(db: Session):
    return db.query(models.Travelpoint).all()