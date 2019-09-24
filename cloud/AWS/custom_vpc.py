#!/usr/bin/env-python3
import boto3
ec2 = boto3.resource('ec2')
# create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')

#assign a name to our VPC
vpc.create_tags(Tags = [{"Key": "Name", "Value": "my_cli_vpc"}])
vpc.wait_until_available()

# enable public dns hostname so that we can SSH into it later

ec2client = boto3.client('ec2')
ec2client.modify_vpc_attribute(VpcId = vpc.id, EnableDnsSupport = {'Value': True})
ec2client.modify_vpc_attribute(VpcId = vpc.id, EnableDnsHostnames = {'Value': True}) 

# create an internet gateway and attach it to VPC
internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

# create a route table and a public route
routetable = vpc.create_route_table()
route = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)

#create subnet and associate it with route table
subnet = ec2.create_subnet(CidrBlock='10.0.0.0/24', VpcId = vpc.id)
routetable.associate_with_subnet(SubnetId = subnet.id)

# Create a security group and allow SSH inbound rule through the VPC
securitygroup = ec2.create_security_group(GroupName = 'SSH-ONLY', Description='only allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)

# Create a linux instance in the subnet
instance = ec2.create_instances(
    ImageId = 'ami-0d2692b6acea72ee6',
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1,
    NetworkInterfaces = [{
        'SubnetId': subnet.id,
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True,
        'Groups': [securitygroup.group_id]
    }],
    KeyName = 'ec2-keypair'
)