import boto3


def stop_instance(instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(response)


stop_instance("i-0c8028b8450586ee3")
