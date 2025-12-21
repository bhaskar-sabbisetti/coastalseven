import redis
import time
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
redis_client.ping()
redis_client.set("name","bhaskar")
print(redis_client.get("name"))
redis_client.setex("otp",10,"1234")
print(redis_client.ttl("otp"))
time.sleep(5)
print(redis_client.get("otp"))
time.sleep(6)
print(redis_client.get("otp"))
