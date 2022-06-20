import boto3

bucket_name = "boto-lesson-255415"
s3 = boto3.client("s3")


def upload_file(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"{file_name} has benn uploaded to {bucket_name} bucket successfully")


upload_file("hello.txt", bucket_name)

# Resource
# bucket_name = "boto-lesson-255415"
# s3 = boto3.resource("s3")


# def upload_file(file_name, bucket, object_name=None, args=None):
#     if object_name is None:
#         object_name = file_name
#     s3.meta.client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
#     print(f"{file_name} has benn uploaded to {bucket_name} bucket successfully")


# upload_file("hello.txt", bucket_name)
