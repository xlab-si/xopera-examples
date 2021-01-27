import json
import logging
import os

import azure.functions as func
from PIL import Image

from .azure_helper import Azure

'''
Azure function for watermarking images
Gets image from container, watermarks it and stores it into destination container. Both containers must exist for smooth execution.
'''

# environment variables
conn_str = os.getenv('CONNECT_STR')
container_out_name = os.getenv('CONTAINER_OUT_NAME')


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    watermark_path = f'{context.function_directory}/watermark.png'

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
                create_watermark(blob=blob, container=container_name, watermark_path=watermark_path)
                return func.HttpResponse()
    except ValueError:
        pass


def create_watermark(blob, container, watermark_path):
    """
    @param blob: Azure BLOB
    @param container: Azure Container
    @param watermark_path: Path to the watermark
    """
    # get connection string from the environment, then connect to Azure and create Azure client
    azure_object_storage_client = Azure()
    azure_object_storage_client.create_client(azure_connection_string=conn_str)

    # retrieve original image from container
    original_image_path = "/tmp/" + str(blob)
    temp_img = '/tmp/temp-{}'.format(blob)
    azure_object_storage_client.retrieve_from_bucket(container, blob)

    # get blob name without the (.jpg) extension and watermark image
    blob_name = os.path.splitext(blob)[0]
    watermark_image(original_image_path, temp_img, watermark_path)
    dest_file_name = blob_name + "-watermarked" + ".jpg"

    # store thumbnail to bucket(container)
    azure_object_storage_client.store_to_bucket(container_out_name, dest_file_name, temp_img)


def watermark_image(original_img_path, watermarked_img_path, watermark_path):
    """
    :param original_img_path: Path of the image to be watermarked
    :param watermarked_img_path: Path for the watermarked image
    :param watermark_path: Path to the watermark
    :return: Returns, when image is saved to watermarked_img_path
    """
    with Image.open(original_img_path) as image:
        with Image.open(watermark_path) as wm:
            org_width = image.width
            org_height = image.height
            wm_width = wm.width
            wm_height = wm.height
            img_wm = image
            padding = 20
            if org_width >= wm_width + padding and org_height >= wm_height + padding:
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
