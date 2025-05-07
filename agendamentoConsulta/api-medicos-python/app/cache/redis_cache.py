from functools import wraps
from redis import Redis
from app.config import settings
import pickle
import hashlib
from fastapi import Request

redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD or None,
    db=settings.REDIS_DB,
    decode_responses=False
)

def cache(key_prefix: str = "medico", ttl: int = 300):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            # Gera chave única para o cache
            cache_key = f"{key_prefix}:{hashlib.md5(str(kwargs).encode()).hexdigest()}"
            
            # Tenta obter do cache
            cached_data = redis_client.get(cache_key)
            if cached_data:
                return pickle.loads(cached_data)
                
            # Se não em cache, executa a função
            result = await func(request, *args, **kwargs)
            
            # Armazena no cache
            redis_client.setex(cache_key, ttl, pickle.dumps(result))
            return result
        return wrapper
    return decorator

def invalidate_cache(key_prefix: str):
    """Remove todos os itens do cache com o prefixo especificado"""
    keys = redis_client.keys(f"{key_prefix}:*")
    if keys:
        redis_client.delete(*keys)
