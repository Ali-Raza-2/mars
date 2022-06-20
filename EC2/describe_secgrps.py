from pprint import pprint
import boto3

ec2 = boto3.client("ec2")
response = ec2.describe_security_groups()
pprint(response)
