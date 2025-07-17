import boto3

ec2 = boto3.client("ec2")

volume_id = "vol-049df61146c4d7901"  # Replace with your volume ID

response = ec2.create_snapshot(
    VolumeId=volume_id, Description="Automated backup snapshot"
)

print(f"Snapshot created with ID: {response['SnapshotId']}")
