import boto3

s3 = boto3.client("s3")
response = s3.delete_object(
    Bucket="boto-lesson-255415",
    Key="hello.txt"
)
print(response)


# Delete Multiple Files

# response = s3.delete_objects(
#     Bucket="boto-lesson-255415",
#     Delete={
#         "Objects": [

#             {
#                 "Key": "ad-hoc.txt",

#             },
#             {
#                 "Key": "hello.txt"
#             },
#             {
#                 "Key": "slacktoken.txt"
#             }
#         ]
#     }
# )

# print(response)
