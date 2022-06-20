import boto3

ec2 = boto3.client("ec2")
response = ec2.authorize_security_group_ingress(
    GroupId="sg-0e7094083c0921242",
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "Allow access from anywhere"}]
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "Allow ssh from anywhere"}]
        }
    ]

)

print(response)
