from wand.image import Image
from google.cloud import storage
import os

''' 
GCP function for thumbnail generation
Gets image from source bucket, resizes it and stores it into destination bucket. 
Both buckets must exist for smooth execution.
Set thumbnail sizes in THUMBNAIL_SIZES_PX
'''

THUMBNAIL_SIZES_PX = [100, 160, 200]
# environment variables
bucket_out_name = os.getenv('BUCKET_OUT_NAME')

# create GCP storage client
client = storage.Client()


def entry_point(data, context):
    """
    Creates image thumbnails from source bucket and stores it to destination bucket
    @param data: The Cloud Functions event payload.
    @param context: Metadata of triggering event.
    @type data dict
    @type context google.cloud.functions.Context
    """
    bucket_in_name = data['bucket']
    key = data['name']
    bucket_in = client.get_bucket(bucket_in_name)
    bucket_out = client.get_bucket(bucket_out_name)

    # Download the image
    image = Image(blob=bucket_in.get_blob(key).download_as_string())

    for size_px in THUMBNAIL_SIZES_PX:
        key_tuple = os.path.splitext(key)
        dest_file_name = key_tuple[0] + "-resized-" + str(size_px)
        if len(key_tuple) == 2:
            dest_file_name += key_tuple[1]
        # Resize the image
        image.resize(size_px, size_px)
        # Upload the thumbnail with the filename prefix
        thumbnail_blob = bucket_out.blob(dest_file_name)
        thumbnail_blob.upload_from_string(image.make_blob())
