import redis
import os
from functools import wraps
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL)

def cache_response(ttl=60 * 60):  # 1 hora padrão
    def decorator(f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            key = f"medicos:{f.__name__}:{str(kwargs)}"
            
            # Verifica cache
            cached = redis_client.get(key)
            if cached:
                return json.loads(cached)
                
            # Executa a função se não tiver cache
            result = await f(*args, **kwargs)
            
            # Armazena no cache
            redis_client.setex(key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator

def invalidate_cache(pattern="medicos:*"):
    keys = redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)