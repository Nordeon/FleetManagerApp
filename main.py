from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "API is running"}


@app.get("/vehicle/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    return {"id": vehicle_id, "year": "2010", "make": "Ford", "model": "F-150", "status": True}