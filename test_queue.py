import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True  # Automatically decode byte responses to strings
)

redis_client.lpush('document_queue', 'resume.pdf')
print("Task added to the queue. ")