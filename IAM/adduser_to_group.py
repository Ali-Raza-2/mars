import boto3


def adduser_to_group(username, group_name):
    iam = boto3.client("iam")
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )

    print(response)


adduser_to_group("cuteuser", "RDS-Admins")
