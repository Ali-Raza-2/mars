import boto3


def delete_user(username):
    iam = boto3.client("iam")
    response = iam.delete_user(
        UserName=username

    )
    print(response)


delete_user("cuteuser")


# To delete a user detach policy first,
# remove it from group and delete Access Key.
