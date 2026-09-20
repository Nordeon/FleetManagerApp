from fastapi import FastAPI, Body, HTTPException, status
from vehicle_information import VehicleInformation
from trip_information import Trip
from driver_information import DriverInformation
from location_ping import LocationPing

app = FastAPI()
vehicles = []
drivers = []
trips = []
last_updates = {}

@app.get("/")
def hello():
    return {"message": "API is running"}

@app.post("/vehicles", status_code=status.HTTP_201_CREATED)
def create_vehicle(v_info: VehicleInformation):
    """
        processes vehicle information such as vehicle_name, 
        vehicle_make, vehicle_model, vehicle_vin
    """
    vehicle_id = check_valid_id(v_info.vehicle_id)
    vehicle = {"id": vehicle_id, "vehicle_name": v_info.vehicle_name, "make":v_info.vehicle_make, "model": v_info.vehicle_model, "vin": v_info.vehicle_vin, "status": v_info.vehicle_status}
    vehicles.append(vehicle)
    return vehicle

"""
    POST & GET for vehicles
"""

@app.get("/vehicles")
def vehicle_list():
    return vehicles

@app.delete("/vehicles/{vehicle_id}")
def remove_vehicle(vehicle_id: int):
    for v in vehicles:
        if v["id"] == vehicle_id:
            vehicles.remove(v)
            return {"message": f"vehicle with ID {vehicle_id} has been removed"}
    raise HTTPException(status_code=404, detail="vehicle not found")   

def check_valid_id(id):
    for v in vehicles:
        if v["id"] == id:
                raise HTTPException(status_code=409, detail=f"Vehicle with ID {id} already exists.")   

    return id

"""
    POST & GET for Trips
"""

@app.get('/trips')
def get_trip():
    return trips

@app.post('/trips/create', status_code=status.HTTP_201_CREATED)
def create_trip(trip: Trip):
    if not any(v["id"] == trip.vehicle_id for v in vehicles) or not any(d["id"] == trip.driver_id for d in drivers):
        raise HTTPException(status_code=404, detail="Vehicle or driver isn't found")


    vehicle_history = {"driver": trip.driver_id, "vehicle": trip.vehicle_id, "start_time": trip.start_time, "end_time": trip.end_time}
    trips.append(vehicle_history)
    return vehicle_history

"""
    CRUD for drivers
"""

@app.get('/drivers')
def get_drivers():
    return drivers

@app.post('/drivers/create', status_code=status.HTTP_201_CREATED)
def create_driver(info: DriverInformation):
    driver = {"driver_id": info.driver_id, "driver_name": info.driver_name}
    drivers.append(driver)
    return driver

@app.delete('/drivers/{driver}', status_code=status.HTTP_202_ACCEPTED)
def delete_driver(id: str):
    for d in drivers:
        if d["driver_id"] == id:
            drivers.remove(d)
            return {"message": f"Driver with ID {id} has been removed."}

    raise HTTPException(status_code=404, detail=f"Cannot find driver {id}.")

"""
    CRUD for Location Pinging
"""

@app.get('/ping/{vehicle_id}')
def get_vehicle_location(vehicle_id: str):
    if vehicle_id in last_updates.keys():
        return last_updates.get(vehicle_id)
    else:
        raise HTTPException(status_code=404, detail=f"Last location for vehicle {vehicle_id} cannot be found")

@app.post('/ping/create', status_code=status.HTTP_201_CREATED)
def create_vehicle_location(ping: LocationPing):
    if not any(v["id"] == ping.vehicle_id for v in vehicles): 
     raise HTTPException(status=404, detail=f"Vehicle {ping.vehicle_id} can't be found")

    detail = {
    "lat": ping.lat, 
    "long": ping.long,
    "address": ping.address,
    "timestamp": ping.timestamp
    }

    last_updates[ping.vehicle_id] = detail

    return detail
