
from fastapi import APIRouter , Depends
from pydantic import BaseModel
from app.core.dependancies import get_api_key, get_currant_user
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFetures(BaseModel):
    car_id: str
    year: int
    age: int
    engine_cc: int
    mileage_kmpl: float
    km_driven: int
    owner_count: int
    brand: str
    model: str
    fuel_type: str
    transmission: str
    city: str

@router.post('/predict')   
def predict_price(car:CarFetures, user= Depends(get_currant_user), _=Depends((get_api_key))):
    prediction = predict_car_price(car.model_dump()) 
    return {'predicted_price': prediction}
  

