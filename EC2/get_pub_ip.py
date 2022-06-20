import boto3


def get_ip(instance_id):
    ec2 = boto3.client("ec2")
    reservations = ec2.describe_instances(
        InstanceIds=[instance_id]).get("Reservations")
    for reservation in reservations:
        for instance in reservation["Instances"]:
            print(instance.get("PublicIpAddress"))


get_ip()
