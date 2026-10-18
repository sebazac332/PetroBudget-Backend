from pydantic import BaseModel
from typing import Optional
from app.model.models import fuelTypeEnum

class FuelBase(BaseModel):
    fuel_type: fuelTypeEnum
    price_per_gallon: float
    fuel_station: str


class FuelCreate(FuelBase):
    user_id: int

class FuelUpdate(BaseModel):
    fuel_type: Optional[fuelTypeEnum] = None
    price_per_gallon: Optional[float] = None
    fuel_station: Optional[str] = None

class Fuel(FuelBase):
    fuel_id: int

    class Config:
        from_attributes = True