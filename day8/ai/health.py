from redis_client import redis_client

def check_health():
    try:
        redis_client.ping()
        return {
            "status": "ok",
            "redis": "up"
        }
    except Exception:
        return {
            "status": "degraded",
            "redis": "down"
        }
