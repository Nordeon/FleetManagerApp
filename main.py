from fastapi import FastAPI, Body, HTTPException, status
from vehicle_information import VehicleInformation
from trip_information import Trip
from driver_information import DriverInformation
from location_ping import LocationPing

app = FastAPI()
vehicles = []
drivers = []
vehicle_history ={}
last_updates = []

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
    vehicle = {"id": vehicle_id, "make":v_info.vehicle_make, "model": v_info.vehicle_model, "vin": v_info.vehicle_vin, "status": v_info.vehicle_status}
    vehicles.append(vehicle)

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
    return vehicle_history

@app.post('/trips/create')
def create_trip(trips: Trip):
    vehicle_history[trips.vehicle_id] = {"driver": trips.driver_id, "start_time": trips.start_time, "end_time": trips.end_time}

"""
    CRUD for drivers
"""

@app.get('/drivers')
def get_drivers():
    return drivers

@app.post('/drivers/create')
def create_driver(info: DriverInformation):
    driver = {"driver": info.driver_name, "vehicle": info.vehicle_id}
    drivers.append(driver)

@app.delete('drivers/{driver}', status_code=status.HTTP_202_ACCEPTED)
def delete_driver(driver: str):
    for d in drivers:
        if d["driver"] == driver:
            drivers.remove(d)
            return {"message": f"{driver} has been removed."}

"""
    CRUD for Location Pinging
"""

@app.get('/ping/{vehicle_id}')
def get_vehicle_location(vehicle_id: str):
    for pings in last_updates:
        if pings["vehicle"] == vehicle_id:
            #last_coordinate = (last_updates["lat"], last_updates["long"])
            return pings

@app.post('/ping/create')
def create_vehicle_location(ping: LocationPing):
    p = {"vehicle": ping.vehicle_id, 
         "lat": ping.lat, 
         "long": ping.long,
         "address": ping.address,
         "timestamp": ping.timestamp.now()}

    last_updates.append(p)