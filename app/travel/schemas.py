from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional

class TravelBase(BaseModel):
    travel_date: date
    total_cost: float
    total_distance: Decimal

class TravelCreate(TravelBase):
    user_id: int
    vehicle_plate: str
    fuel_id: int

class TravelUpdate(BaseModel):
    travel_date: Optional[date] = None
    total_cost: Optional[float] = None
    total_distance: Optional[Decimal] = None

class Travel(TravelBase):
    travel_id: int

    class Config:
        orm_mode = True