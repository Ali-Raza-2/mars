import boto3

ec2 = boto3.client("ec2")
response = ec2.create_security_group(
    Description="web access secgrp-boto",
    GroupName="boto-sg-group",
    VpcId="vpc-01860f03ded8eb5dc"

)

print(response)
