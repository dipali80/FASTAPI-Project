
import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cache_prediction, get_cached_prediction

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data:dict):
    



