from fastapi import FastAPI, Body
from vehicle_information import VehicleInformation

app = FastAPI()
vehicles = []

@app.get("/")
def hello():
    return {"message": "API is running"}

@app.post("/vehicles")
def create_vehicle(v_info: VehicleInformation = Body(embed=True)):
    """
        processes vehicle information such as vehicle_name, 
        vehicle_make, vehicle_model, vehicle_vin
    """
    vehicle = {"id": len(vehicles)+1, "make":v_info.vehicle_make, "model": v_info.vehicle_model, "vin": v_info.vehicle_vin, "status": "Active"}
    vehicles.append(vehicle)
    return vehicle

@app.get("/vehicles")
def vehicle_list():
    return vehicles

@app.delete("/vehicles/{vehicle_id}")
def remove_vehicle(vehicle_id: int):
    for v in vehicles:
        if v["id"] == vehicle_id:
            vehicles.remove(v)
            return {"message": f"vehicle with ID {vehicle_id} has been removed"}
    return {"message": "vehicle not found"}, 404    