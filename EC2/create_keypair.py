from pprint import pprint
import boto3

ec2 = boto3.client("ec2")
response = ec2.create_key_pair(
    KeyName="hello",
    KeyType="rsa"
)

file = open("hello.pem", "w")
file.write(response["KeyMaterial"])
file.close()

print("Key Created Successfully!")
