import boto3
#configure connection using custom profile instead of default profile via aws cli
boto3.setup_default_session(profile_name='tecnotes2')
AWS_REGION = "us-east-1"
#define the connection 
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
VOLUME_ID = 'vol-0eefa80b9976736eb'

snapshot = EC2_RESOURCE.create_snapshot(
VolumeId=VOLUME_ID,
TagSpecifications=[
{
'ResourceType': 'snapshot',
'Tags': [
{
'Key': 'Name',
'Value': 'hands-on-cloud-ebs-snapshot'
},
]
},
]
)