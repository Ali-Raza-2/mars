import boto3


def terminate_instance(Instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.terminate_instances(InstanceIds=[Instance_id])
    print(response)


terminate_instance("i-068d5cabaa01986de")
