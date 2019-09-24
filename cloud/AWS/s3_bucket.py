#!/usr/bin/env-python3
import logging
import boto3
import json
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


def upload_file(file_name, bucket, object_name=None):
    #If s3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def download_file(bucket_name, object_name, file_name):
    #If s3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket_name, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Retrieve the policy of the specified bucket
'''
bucket_name = 'bucket_name'
bucket_policy = {
    'Version': '2019-7-12',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::bucket_name/*'
    }]
}
# Convert the policy from JSON dict to string


# set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy('bucket_name', Policy=bucket_policy)
'''
s3 = boto3.client('s3')
result = s3.get_bucket_acl(Bucket='bucket_name')
print(result)

  

    
