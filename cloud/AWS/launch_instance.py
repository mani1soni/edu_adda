#!/usr/bin/python3
import boto3
ec2 = boto3.resource('ec2')
# create a new EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0d2692b6acea72ee6',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='ec2-keypair'
)
