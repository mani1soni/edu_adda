#!/usr/bin/python3
import boto3
ec2 = boto3.resource('ec2')

# create a file to store the key locally
outfile = open('ec2-keypair.pem','w')

#call the boto ec2 function to create a key pair 
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

# capture the key and store it in a file 
key_pair_out = str(key_pair.key_material)
print(key_pair_out)
outfile.write(key_pair_out)


