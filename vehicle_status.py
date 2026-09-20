from enum import Enum
class VehicleStatus(Enum):
    """
        - ON: vehicle ignition is on
        - IDLE: vehicle is ON and it has been in the same location for a minute
        - MOVING: vehicle is ON and moving
        - IN_MAINTENANCE: a manual setting that says that a vehicle is currently being serviced
        - OFF: vehicle ignition is off
    """
    
    ON = 'status_on'
    IDLE = 'status_idle'
    MOVING = 'status_moving'
    IN_MAINTENANCE = 'status_maintenance'
    OFF = 'status_off'