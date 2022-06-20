import boto3

bucket_name = "boto-lesson-255415"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
print("----Listing all the objects in the bucket----")
for object in bucket.objects.all():
    print(object.key)
