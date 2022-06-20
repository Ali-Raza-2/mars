import boto3


def create_bucket(bucket_name, acl):
    s3 = boto3.client("s3")
    response = s3.create_bucket(
        Bucket=bucket_name,
        ACL=acl,
        CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        }
    )
    print(f'Bucket "{bucket_name}" created Successfully.')


create_bucket("boto-lesson-255415", "private")
# Resource
# def create_bucket(bucket_name, acl):
#     bucket = boto3.resource("s3")
#     response = bucket.create_bucket(
#         Bucket=bucket_name,
#         ACL=acl,
#         CreateBucketConfiguration={
#             "LocationConstraint": "ap-south-1"
#         }
#     )
