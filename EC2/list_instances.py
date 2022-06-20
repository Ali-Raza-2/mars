import boto3


def get_instances():
    ec2 = boto3.client("ec2")
    reservations = ec2.describe_instances().get("Reservations")
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            if instance["State"]["Name"] == "running":
                print("------------------------------------------------")
                instance_name = instance["Tags"][0]["Value"]
                instance_id = instance["InstanceId"]
                instance_state = instance["State"]["Name"]
                ami_id = instance["ImageId"]
                instance_type = instance["InstanceType"]
                vpc_id = instance["VpcId"]
                subnet_id = instance["SubnetId"]
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
                availability_zone = instance["Placement"]["AvailabilityZone"]
                secgrp_name = instance["SecurityGroups"][0]["GroupName"]
                secgrp_id = instance["SecurityGroups"][0]["GroupId"]
                print(f"instance_name: {instance_name}\ninstance_state: {instance_state}\ninstance_id: {instance_id}\ninstance_type: {instance_type}\nami_id: {ami_id}\nvpc_id: {vpc_id}\nsubnet_id: {subnet_id}\navailability_zone: {availability_zone}\nsecgrp_name: {secgrp_name}\nsecgrp_id: {secgrp_id}\npublic_ip: {public_ip}\nprivate_ip: {private_ip}")
                print("------------------------------------------------")
            else:
                print(
                    f"The Instance {instance_id} is not running!")


get_instances()
