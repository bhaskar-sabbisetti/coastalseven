from redis_client import redis_client

RATE_LIMIT = 5
WINDOW = 60


def is_rate_limited(client_id: str) -> bool:
    key = f"rate:{client_id}"
    count = redis_client.incr(key)

    if count == 1:
        redis_client.expire(key, WINDOW)

    return count > RATE_LIMIT
