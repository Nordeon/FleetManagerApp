from pydantic import BaseModel

class DriverInformation(BaseModel):
    """
        needs to validate driver_id against existing IDs, spaces, and symbols
    """
    driver_id: str
    driver_name: str