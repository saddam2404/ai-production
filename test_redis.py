import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True  # Automatically decode byte responses to strings
)

print(redis_client.ping())  # Should return True if the connection is successful