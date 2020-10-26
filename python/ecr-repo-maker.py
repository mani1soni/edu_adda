#!/usr/bin/python3
import boto3

client = boto3.client('ecr')

APP_NAME = ['repo-1','repo-2','repo-3','repo-4','repo-5']
ENV = ['production','staging']
stage = ['backup','deploy']


for i in APP_NAME:
    for j in ENV:
        for k in stage:
            if j=='production' and k=='deploy':
                exit
            elif j=='staging' and k=='backup':
                exit
            else:
                response = client.create_repository(
                    repositoryName=i+'-'+j+'-'+k
                )
            
