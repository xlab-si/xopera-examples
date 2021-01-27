import os

import boto3
from azure_helper import Azure

s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
transfer_bucket_name = os.getenv('TRANSFER_BUCKET_NAME')


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        blob = record['s3']['object']['key']

        original_img = '/tmp/neza-resized-{}'.format(blob)
        print("bucket: " + str(bucket))
        print("blob: " + str(blob))
        s3_client.download_file(bucket, blob, original_img)

        conn_str = os.getenv('CONNECT_STR')
        azure_object_storage_client = Azure()
        azure_object_storage_client.create_client(azure_connection_string=conn_str)
        azure_object_storage_client.store_to_bucket(transfer_bucket_name, blob, original_img)
