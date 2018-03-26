#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

bucketName = 'bondit'
key = 'upload_test.txt'

s3 = boto3.resource('s3')
try:
    s3.Bucket(bucketName).download_file("EC2_files/"+key, "qa_download_test.txt")
except ClientError as error:
    print("Error with file downloading: %s" %error)
except:
    print("Unknown error with file uploading")
