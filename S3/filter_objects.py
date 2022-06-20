import boto3

bucket_name = "boto-lesson-255415"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
print("---Getting your Object---")
for object in bucket.objects.filter(Prefix="slacktoken.txt"):
    print(object.key)
