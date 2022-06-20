import boto3

s3 = boto3.resource("s3")

copy_source = {
    "Bucket": "boto-lesson-255415",
    "Key": "hello.txt"

}

s3.meta.client.copy(copy_source, "art-of-jenkins", "copied-hello.txt")
print("Object Copied Successfully!")
