import boto3


def list_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket["Name"])


list_buckets()

# Resource
# def list_buckets():
#     s3 = boto3.resource("s3")
#     collection = s3.buckets.all()
#     for bucket in collection:
#         print(bucket.name)
