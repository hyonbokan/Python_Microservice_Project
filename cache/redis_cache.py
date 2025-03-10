import json
import redis
from utils.config import Config
from utils.interfaces import CacheService

class RedisCacheService(CacheService):
    def __init__(self):
        self.client = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            db=Config.REDIS_DB,
            decode_responses=True
        )
        
    def save(self, key, value, expiry=60):
        self.client.setex(key, expiry, json.dumps(value, default=str))
    
    def get(self, key):
        data = self.client.get(key)
        return json.loads(data) if data else None