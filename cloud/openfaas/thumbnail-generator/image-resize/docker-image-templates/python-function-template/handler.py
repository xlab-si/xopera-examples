import json
from PIL import Image
from .minio_helper import MinIO

''' 
OpenFaaS function for thumbnail generation
Gets image from source bucket and stores it into destination bucket. Both buckets must exist for smooth execution.
Set thumbnail sizes in THUMBNAIL_SIZES_PX
'''

# thumbnail sizes
THUMBNAIL_SIZES_PX = [100, 160, 200]

# templating variables
node_ip = "{{ host_ip }}"
minio_access_key = "{{ credentials.minio_access_key }}"
minio_secret_key = "{{ credentials.minio_secret_key }}"
source_bucket = "{{ bucket_in_name }}"
dest_bucket = "{{ bucket_out_name }}"

# create MinIO client
minio_client = MinIO()
minio_client.create_client(ip=node_ip, access_key=minio_access_key, secret_key=minio_secret_key)


def convert_push(file_name):
    """
    Creates image thumbnails from source bucket and stores it to destination bucket
    @param file_name: File name with source image
    @type file_name str
    """
    minio_client.retrieve_from_bucket(source_bucket, file_name)
    original_img = '/tmp/{}'.format(file_name)
    temp_img = '/tmp/resize-{}'.format(file_name)

    for size_px in THUMBNAIL_SIZES_PX:
        resize_image(original_img, temp_img, size_px)
        dest_file_name = file_name.replace(".jpg", "") + "-resized-" + str(size_px)
        minio_client.store_to_bucket(dest_bucket, dest_file_name, temp_img)


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


def handle(st):
    """
    Main function handler
    @param st: Request
    @type st: str
    """
    req = json.loads(st)

    for obj in req['Records']:
        filename = obj['s3']['object']['key']
        convert_push(source_bucket)
