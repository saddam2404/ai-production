import redis
from app.aws import s3_client, BUCKET_NAME

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True  # Automatically decode byte responses to strings
)
while True:
    task = redis_client.brpop('document_queue', timeout=0)  # Wait indefinitely for a task
    filename = task[1]

    file_path = f"downloads/{filename}"

    print("Processing task:", task[1])