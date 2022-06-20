import boto3


def detach_policy(username, policy_arn):
    iam = boto3.client("iam")
    response = iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)


detach_policy("cuteuser", "arn:aws:iam::250897854889:policy/pyFullAcess")
