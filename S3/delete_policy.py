import boto3

s3 = boto3.client("s3")
response = s3.delete_bucket_policy(Bucket="boto-lesson-255415")
print(response)
