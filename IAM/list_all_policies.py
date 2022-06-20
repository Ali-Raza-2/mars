import boto3


def list_all_policies():
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_policies")
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            policy_name = policy["PolicyName"]
            Arn = policy["Arn"]
            print(f"Policy Name:- {policy_name} ||\n Arn:- {Arn}")


list_all_policies()

# We can also set Scope to AWS to list all AWS Managed Policies
