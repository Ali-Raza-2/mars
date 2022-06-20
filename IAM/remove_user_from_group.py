import boto3


def remove_user_from_group(username, group_name):
    iam = boto3.resource("iam")
    group = iam.Group(group_name)
    response = group.remove_user(
        UserName=username
    )

    print(response)


remove_user_from_group("cuteuser", "RDS-Admins")
