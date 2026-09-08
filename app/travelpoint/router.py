from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models

router = APIRouter(prefix="/travels", tags=["Travels"])

@router.post("/", response_model=schemas.Travelpoint)
def register_travelpoint(travelpoint: schemas.TravelpointCreate, db: Session = Depends(get_db)):
    if functions.get_travelpoint_by_id(db, travelpoint.point_id):
        raise HTTPException(status_code=400, detail="A travel point with this ID already exists.")
    return functions.create_travelpoint(db, travelpoint)

@router.put("/{point_id}", response_model=schemas.Travelpoint)
def edit_travelpoint(point_id: int, travelpoint_update: schemas.TravelpointUpdate, db: Session = Depends(get_db)):
    travelpoint = functions.update_travelpoint(db, point_id, travelpoint_update)
    if not travelpoint:
        raise HTTPException(status_code=404, detail="Travel point not found")
    return travelpoint

@router.delete("/{point_id}", response_model=schemas.Travelpoint)
def remove_travelpoint(point_id: int, db: Session = Depends(get_db)):
    travelpoint = functions.delete_travelpoint(db, point_id)
    if not travelpoint:
        raise HTTPException(status_code=404, detail="Travel point not found")
    return travelpoint