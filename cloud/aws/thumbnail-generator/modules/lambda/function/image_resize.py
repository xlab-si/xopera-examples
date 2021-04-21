import os

import boto3
from PIL import Image

''' 
Lambda function for thumbnail generation
Gets image from "<bucket>", stores in "<bucket>-resized". Both buckets must exist for smooth execution.
Set thumbnail sizes in THUMBNAIL_SIZES_PX
'''

THUMBNAIL_SIZES_PX = [100, 160, 200]
# environment variables
bucket_out_name = os.getenv('BUCKET_OUT_NAME')

# create AWS S3 client
aws_s3_client = boto3.client('s3')


def lambda_handler(event, context):
    """
    Creates image thumbnails from source bucket and stores it to destination bucket
    @param event: AWS Event
    @param context: Lambda context
    @type event Union
    @type context AWSLambdaContext
    """
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        original_image_path = '/tmp/{}'.format(key)
        aws_s3_client.download_file(bucket, key, original_image_path)

        for size_px in THUMBNAIL_SIZES_PX:
            resized_image_path = "/tmp/" + str(key) + "_" + str(size_px) + ".jpg"
            resize_image(original_image_path, resized_image_path, size_px)
            dest_file_name = key + "-resized-" + str(size_px) + ".jpg"
            aws_s3_client.upload_file(resized_image_path, bucket_out_name, dest_file_name)


def resize_image(original_img_path, resized_img_path, new_size_px):
    """
    Resizes image and saves it as new file
    @param original_img_path: Path of the original image
    @param resized_img_path: Path for resized image
    @param new_size_px: New size in pixels
    @type original_img_path: str
    @type resized_img_path: str
    @type new_size_px: int
    """
    with Image.open(original_img_path) as image:
        ratio = max(image.size) / float(new_size_px)
        image.thumbnail(tuple(int(x / ratio) for x in image.size))
        image.save(resized_img_path)
