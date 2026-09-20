from pydantic import BaseModel, field_validator
from typing import Optional
from vehicle_status import VehicleStatus

class VehicleInformation(BaseModel):
    vehicle_name: str
    vehicle_id: str
    vehicle_make: Optional[str] = None
    vehicle_model: Optional[str] = None
    vehicle_vin: str
    vehicle_status: VehicleStatus = VehicleStatus.OFF

    @field_validator('vehicle_vin')
    @classmethod
    def validate_vin(cls, value: str) -> str:
        if len(value) != 17:
            raise ValueError(f"VIN is not valid. Length {len(value)}")
        return value