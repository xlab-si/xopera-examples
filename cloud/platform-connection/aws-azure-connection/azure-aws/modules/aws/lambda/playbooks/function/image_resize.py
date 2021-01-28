import os

import boto3
from PIL import Image

s3_client = boto3.client('s3')
bucket_out_name = os.getenv('BUCKET_OUT_NAME')

''' 
Lambda function for thumbnail generation
Gets image from "<bucket>", stores in "<bucket>-resized". Both buckets must exist for smooth execution.
Set thumbnail sizes in THUMBNAIL_SIZES_PX
'''
THUMBNAIL_SIZES_PX = [100, 160, 200]


def resize_image(original_img_path, resized_img_path, new_size_px):
    with Image.open(original_img_path) as image:
        ratio = max(image.size) / float(new_size_px)
        image.thumbnail(tuple(int(x / ratio) for x in image.size))
        image.save(resized_img_path)


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        original_img = '/tmp/original-{}'.format(key)
        temp_img = '/tmp/temp-{}'.format(key)

        print("bucket: " + str(bucket))
        print("key: " + str(key))

        s3_client.download_file(bucket, key, original_img)

        for size_px in THUMBNAIL_SIZES_PX:
            resize_image(original_img, temp_img, size_px)
            new_name_key = key.replace(".jpg", "-resized-" + str(size_px) + ".jpg")
            s3_client.upload_file(temp_img, bucket_out_name, new_name_key)
