from pathlib import Path
import boto3

s3 = boto3.client("s3")

path = Path("/home/ali/py-practice/S3/hello.txt")
data = path.read_text()

response = s3.put_object(
    Bucket="boto-lesson-255415",
    ACL="private",
    Body=data,
    Key="hello.txt"
)


print(response)
