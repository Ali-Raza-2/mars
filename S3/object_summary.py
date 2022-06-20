import boto3

s3 = boto3.resource("s3")
object_summary = s3.ObjectSummary("boto-lesson-255415", "hello.txt")
print(object_summary)
