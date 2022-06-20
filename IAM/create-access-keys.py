import boto3


def create_access_key(username):
    iam = boto3.client("iam")
    response = iam.create_access_key(
        UserName=username
    )
    print(response)


create_access_key("cuteuser")
