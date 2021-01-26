from PIL import Image
import boto3
import os

s3_client = boto3.client('s3')
# get env var for bucket with results
bucket_out_name = os.getenv('BUCKET_OUT_NAME')

'''
Lambda function for watermarking images
Gets image from "<bucket>", stores in "<bucket>-watermarked". Both buckets must exist for smooth execution.
'''


def watermark_image(original_img_path, watermarked_img_path):
    """
    :param original_img_path: Path of the image to be watermarked
    :param watermarked_img_path: Path for the watermarked image
    :return: Returns, when image is saved to watermarked_img_path
    """
    with Image.open(original_img_path) as image:
        watermark_path = 'watermark.png'
        with Image.open(watermark_path) as wm:
            org_width = image.width
            org_height = image.height
            wm_width = wm.width
            wm_height = wm.height
            img_wm = image
            padding = 20
            if org_width >= wm_width + padding\
                    and org_height >= wm_height + padding:
                # shift to bottom right with padding
                x_delta = org_width - wm_width - padding
                y_delta = org_height - wm_height - padding
                for x in range(0, wm_width):
                    for y in range(0, wm_height):
                        px = wm.getpixel((x, y))
                        # for transparency to persist
                        if px.count(255) != 3:
                            img_wm.putpixel((x + x_delta, y + y_delta), px)
                img_wm.save(watermarked_img_path)


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        original_img = '/tmp/original-{}'.format(key)
        temp_img = '/tmp/temp-{}'.format(key)

        s3_client.download_file(bucket, key, original_img)

        watermark_image(original_img, temp_img)
        new_name_key = key.replace(".jpg", "_watermarked.jpg")
        s3_client.upload_file(temp_img, bucket_out_name, new_name_key)
