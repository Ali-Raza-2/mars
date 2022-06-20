import boto3

bucket_name = "boto-lesson-255415"
s3 = boto3.resource("s3")
object = s3.Object(bucket_name, "hello.txt")
object.download_file("myfile.txt")
print("File has been downloaded!")
