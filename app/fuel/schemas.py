from pydantic import BaseModel
from typing import Optional

class FuelBase(BaseModel):
    fuel_type: str
    price_per_gallon: float
    fuel_station: str


class FuelCreate(FuelBase):
    user_id: int

class FuelUpdate(BaseModel):
    fuel_type: Optional[str] = None
    price_per_gallon: Optional[float] = None
    fuel_station: Optional[str] = None

class Fuel(FuelBase):
    fuel_id: int

    class Config:
        orm_mode = True