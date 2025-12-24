import hashlib
from redis_client import redis_client

CACHE_TTL = 300  # seconds


def get_cache_key(prompt: str, model_name: str) -> str:
    raw = f"{model_name}:{prompt}"
    return hashlib.sha256(raw.encode()).hexdigest()


def get_cached_response(key: str):
    return redis_client.get(key)


def set_cached_response(key: str, value: str):
    redis_client.setex(key, CACHE_TTL, value)
