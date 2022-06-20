import boto3


def create_login(username, set_password):
    iam = boto3.client("iam")
    login_profile = iam.create_login_profile(
        UserName=username,
        Password=set_password,
        PasswordResetRequired=False,
    )


create_login("someone", "admin@123")
