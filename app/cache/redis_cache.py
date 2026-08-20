
import json
import redis
from app.core.config import settings

redis_clints = redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key:str):
    value = redis_clints.get(key)
    if value: 
        return json.loads(value)
    return None

def set_cache_prediction(key:str, value:dict, expiry:int=3600):
    redis_clints.setex(key, expiry,json.dumps(value))