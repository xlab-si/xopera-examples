import json
import logging
import os
from .azure_helper import Azure

import azure.functions as func
from PIL import Image

'''
Azure function for resizing images
Gets image from container, resizes it and stores it into destination container. Both buckets must exist for smooth execution.
'''

THUMBNAIL_SIZES_PX = [100, 160, 200]
# environment variables
conn_str = os.getenv('CONNECT_STR')
container_out_name = os.getenv('CONTAINER_OUT_NAME')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    SUBSCRIPTION_VALIDATION_EVENT = "Microsoft.EventGrid.SubscriptionValidationEvent"
    CUSTOM_EVENT = "Microsoft.Storage.BlobCreated"

    try:
        postreqdata = req.get_json()

        for event in postreqdata:
            event_data = event['data']

            if event['eventType'] == SUBSCRIPTION_VALIDATION_EVENT:
                validation_code = event_data['validationCode']
                validation_url = event_data.get('validationUrl', None)

                answer_payload = {
                    "validationResponse": validation_code
                }
                return func.HttpResponse(json.dumps(answer_payload))

            elif event['eventType'] == CUSTOM_EVENT:
                print("Got a custom event {} and received {}".format(CUSTOM_EVENT, event_data))
                # get blob url and split it
                blob_url = event_data['url']
                blob_data = blob_url.split("/")
                # get currently added (full) blob name and container name
                blob = blob_data[-1]
                container_name = blob_data[-2]
                # perform thumbnail creation
                create_thumbnails(blob=blob, container=container_name)
                return func.HttpResponse()
    except ValueError:
        pass


def create_thumbnails(blob, container):
    """
    @param blob: Azure BLOB
    @param container: Azure Container
    """
    # get connection string from the environment, then connect to Azure and create Azure client
    azure_object_storage_client = Azure()
    azure_object_storage_client.create_client(azure_connection_string=conn_str)
    # retrieve original image from container
    original_image_path = "/tmp/" + str(blob)
    azure_object_storage_client.retrieve_from_bucket(container, blob)

    for size_px in THUMBNAIL_SIZES_PX:
        # get blob name without the (.jpg) extension and resize image
        blob_name = os.path.splitext(blob)[0]
        resized_image_path = "/tmp/" + str(blob_name) + "_" + str(size_px) + ".jpg"
        resize_image(original_image_path, resized_image_path, size_px)
        dest_file_name = blob_name + "-resized-" + str(size_px) + ".jpg"
        # store thumbnail to bucket
        azure_object_storage_client.store_to_bucket(container_out_name, dest_file_name, resized_image_path)


def resize_image(original_img_path, resized_img_path, new_size_px):
    """
    @param original_img_path: Path of the original image
    @param resized_img_path: Path for resized image
    @param new_size_px: New size in pixels
    """
    with Image.open(original_img_path) as image:
        ratio = max(image.size) / float(new_size_px)
        image.thumbnail(tuple(int(x / ratio) for x in image.size))
        image.save(resized_img_path)
