import boto3


def delete_empty_bucket(bucket_name):
    s3 = boto3.client("s3")
    s3.delete_bucket(Bucket=bucket_name)
    print("The Bucket has been deleted Successfully")


delete_empty_bucket("boto-lesson-255415")

# Delete Bucket with AWS Resource
# s3 = boto3.resource("s3")
# bucket_name = "boto-lesson-255415"
# bucket = s3.Bucket(bucket_name)
# bucket.delete()
# print("The Bucket has been deleted Successfully")
