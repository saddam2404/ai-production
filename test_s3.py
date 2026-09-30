from app.aws import s3_client

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}') 

from app.aws import BUCKET_NAME

print(f'Using bucket: {BUCKET_NAME}')