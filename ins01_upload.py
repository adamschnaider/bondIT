#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

bucketName = 'bondit'
fileName = 'upload_test.txt'
key = 'EC2_filesa/'+fileName
file = open(fileName,'rb')

s3 = boto3.resource('s3')
try:
    s3.Bucket(bucketName).put_object(Key=key,Body=file)
except:
    print("Error with file uploading: %s" %error)
