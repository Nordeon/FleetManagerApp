from pydantic import BaseModel
from typing import Optional

class VehicleInformation(BaseModel):
    vehicle_name: str
    vehicle_make: Optional[str] = None
    vehicle_model: Optional[str] = None
    vehicle_vin: Optional[str] = None