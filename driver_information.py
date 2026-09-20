from pydantic import BaseModel
from typing import Optional

class DriverInformation(BaseModel):
    driver_name: str
    vehicle_id: str