from fastapi import FastAPI
import redis
import time

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.get("/cached-data")
def cached_data():
    cached = redis_client.get("cached_data")

    if cached:
        return {"source": "redis", "data": cached}

    time.sleep(3)  
    data = "Very fast after cache"

    redis_client.setex("cached_data", 30, data)
    return {"source": "db", "data": data}
