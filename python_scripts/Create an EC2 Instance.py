import boto3

ec2 = boto3.resource("ec2")

# Create a new EC2 instance
instances = ec2.create_instances(
    ImageId="ami-0abcdef1234567890",  # Replace with your AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
)

print(f"Created instance with ID: {instances[0].id}")
