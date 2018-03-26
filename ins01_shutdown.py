#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

insIds = ['i-0ef39b36b033fffaa']
ec2 = boto3.resource('ec2')
try:
    ec2.instances.filter(InstanceIds=insIds).stop()
except ClientError as error:
    print ("Error: couldn't power off instance - %s" %error)
