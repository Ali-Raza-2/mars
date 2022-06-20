import boto3


def dettach_group_policy(group_name, policy_arn):
    iam = boto3.client("iam")
    response = iam.detach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    print(response)


dettach_group_policy(
    "RDS-Admins", "arn:aws:iam::aws:policy/AmazonRDSFullAccess")
