from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, Decimal, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Vehicle(Base):
    __tablename__ = "vehicles"

    plate_number = Column(String, primary_key=True, index=True)
    manufacturer = Column(String, unique=False, index=True, nullable=False)
    model = Column(String, unique=False, index=True, nullable=False)
    engine = Column(String, unique=False, index=True, nullable=False)
    fuel_type = Column(String, unique=False, index=True, nullable=False)
    tank_capacity = Column(Float, unique=False, index=True, nullable=False)
    avg_fuel_consumption = Column(Decimal(15, 3), unique=False, index=True, nullable=False)
    wheel_number = Column(Integer, unique=False, index=True, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

class Fuel(Base):
    __tablename__ = "fuels"

    fuel_id = Column(Integer, primary_key=True, index=True)
    fuel_type = Column(String, unique=False, index=True, nullable=False)
    price_per_gallon = Column(Float, unique=False, index=True, nullable=False)
    fuel_station = Column(String, unique=True, index=True, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

class Travel(Base):
    __tablename__ = "travels"

    travel_id = Column(Integer, primary_key=True, index=True)
    travel_date = Column(Date, unique=False, index=True, nullable=False)
    total_cost = Column(Float, unique=False, index=True, nullable=False)
    total_distance = Column(Decimal(15, 3), unique=False, index=True, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    vehicle_plate = Column(String, ForeignKey("vehicles.plateNumber"), nullable=False)

    fuel_id = Column(Integer, ForeignKey("fuels.fuel_id"), nullable=False)

class Travelpoint(Base):
    __tablename__ = "travelpoints"

    point_id = Column(Integer, primary_key=True, index=True)
    point_name = Column(String, unique=False, index=True, nullable=False)
    distance_from_last_point = Column(Decimal(15, 3), unique=False, index=True, nullable=False)

    last_point_id = Column(Integer, ForeignKey("travelpoints.point_id"), nullable=True)

    travel_id = Column(Integer, ForeignKey("travels.travel_id"), nullable=False)