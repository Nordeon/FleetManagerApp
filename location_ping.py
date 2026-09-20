from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime 

class LocationPing(BaseModel):
    """
        - lat: latitude of vehicle
        - long: longitude of vehicle
        - address: where the vehicle has been based on the coordinates
    """
    lat: float
    long: float

    vehicle_id: str
    timestamp: datetime
    address: Optional[str] = ""

    @field_validator('lat')
    @classmethod
    def validate_lat(cls, val):
        if val < -90 or val > 90:
            raise ValueError("Latitude is not valid")
        return val

    @field_validator('long')
    @classmethod
    def validate_long(cls, val):
        if val < -180 or val > 180:
            raise ValueError("Longitude is not valid")
        return val