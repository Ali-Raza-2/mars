import boto3


def create_group(groupname):
    iam = boto3.client("iam")
    iam.create_group(GroupName=groupname)


create_group("RDS-Admins")
