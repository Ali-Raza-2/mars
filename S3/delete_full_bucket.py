import boto3

bucket_name = "boto-lesson-255415"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)


def clean_up():
    # for all objects in the bucket
    for object in bucket.objects.all():
        object.delete()

    # for versioned objects  in the bucket
    for object_ver in bucket.object_versions.all():
        object_ver.delete()

    print("The Bucket is fully Cleaned")


clean_up()
bucket.delete()
print("The Bucket has been deleted Successfully")
