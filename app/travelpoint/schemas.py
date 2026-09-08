from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class TravelpointBase(BaseModel):
    point_name: str
    distance_from_last_point: Decimal

class TravelpointCreate(TravelpointBase):
    last_point_id: Optional[int] = None
    travel_id: int

class TravelpointUpdate(BaseModel):
    point_name: Optional[str] = None
    distance_from_last_point: Optional[Decimal] = None
    last_point_id: Optional[int] = None

class Travelpoint(TravelpointBase):
    point_id: int

    class Config:
        orm_mode = True