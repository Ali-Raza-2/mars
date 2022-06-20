import boto3


def attach_policy(username, policy_arn):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)


attach_policy("cuteuser", "arn:aws:iam::250897854889:policy/pyFullAcess")
