import boto3

ec2 = boto3.client("ec2")
response = ec2.delete_security_group(GroupId="sg-092a669e243e04cc9")
print(response)
