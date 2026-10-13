from app.aws import s3_client, BUCKET_NAME

response = s3_client.list_objects_v2(
    Bucket=BUCKET_NAME
)

for obj in response.get("Contents", []):
    print(obj["Key"])
    