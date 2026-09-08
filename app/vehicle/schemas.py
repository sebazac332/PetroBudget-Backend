from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    manufacturer: str
    model: str
    engine: str
    fuel_type: str
    tank_capacity: float
    avg_fuel_consumption: float
    wheel_number: int

class VehicleCreate(VehicleBase):
    user_id: int

class VehicleUpdate(BaseModel):
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    engine: Optional[str] = None
    fuel_type: Optional[str] = None
    tank_capacity: Optional[float] = None
    avg_fuel_consumption: Optional[float] = None
    wheel_number: Optional[int] = None

class Vehicle(VehicleBase):
    plate_number: str

    class Config:
        orm_mode = True