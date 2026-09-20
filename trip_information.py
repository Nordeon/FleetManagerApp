from pydantic import BaseModel, model_validator
from datetime import datetime

class Trip(BaseModel):
    """
     - start_time: the time where a vehicle has started its trip
     - end_time: the time where a vehicle has finished its trip
     - vehicle_id: the vehicle linked to this trip
     - driver_id: the driver linked to this trip
    """
    start_time: datetime
    end_time: datetime

    vehicle_id: str
    driver_id: str

    @model_validator(mode='after')
    def validate_trip_time(self) -> datetime:
        if self.end_time < self.start_time:
            raise ValueError("Trip end time is invalid.")
        return self