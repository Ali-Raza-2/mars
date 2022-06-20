import boto3


def update_access_key(username, status, access_key_id):
    iam = boto3.client("iam")
    iam.update_access_key(
        UserName=username,
        Status=status,
        AccessKeyId=access_key_id
    )


update_access_key("cuteuser", "Inactive", "AKIATU2VNOGU4URO4IVG")
