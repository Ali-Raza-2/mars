import boto3

ec2 = boto3.resource("ec2")
response = ec2.create_instances(
    ImageId="ami-08df646e18b182346",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="aliraza14",
    SecurityGroupIds=["sg-0e7094083c0921242"],
    Placement={
        "AvailabilityZone": "ap-south-1a",
        "Tenancy": "default"
    },
    SubnetId="subnet-0f2af2fab0e6bac54",
    UserData="",
    IamInstanceProfile={
        "Arn": "arn:aws:iam::250897854889:instance-profile/myroleprac-ec2"
    },
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "my-web-server"
                }
            ]
        }
    ]
)

print(response)
