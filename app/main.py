from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Import from database

from app.database import engine, Base
from app.model import models
from app.user.router import router as user_router
from app.vehicle.router import router as vehicle_router
from app.fuel.router import router as fuel_router
from app.travel.router import router as travel_router
from app.travelpoint.router import router as travelpoint_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

Base.metadata.create_all(bind=engine)

# Routers

app.include_router(user_router)
app.include_router(vehicle_router)
app.include_router(fuel_router)
app.include_router(travel_router)
app.include_router(travelpoint_router)