import boto3

ec2 = boto3.client("ec2")

instance_id = "i-1234567890abcdef0"  # Replace with your instance ID

response = ec2.start_instances(InstanceIds=[instance_id])

print(f"Starting instance: {instance_id}")
