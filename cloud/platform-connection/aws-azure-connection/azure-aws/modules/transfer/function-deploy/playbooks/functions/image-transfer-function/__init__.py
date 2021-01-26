import json
import logging
import os
import boto3
from .azure_helper import Azure
import azure.functions as func

'''
Azure function for resizing images
Gets image from container, resizes it and stores it into destination container. Both buckets must exist for smooth execution.
'''

THUMBNAIL_SIZES_PX = [100, 160, 200]
# environment variables
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)


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
                transfer_image(blob=blob, container=container_name)
                return func.HttpResponse()
    except ValueError:
        pass


def transfer_image(blob, container):
    """
    @param blob: Azure BLOB
    @param container: Azure Container
    """
    # get connection string from the environment, then connect to Azure and create Azure client
    azure_object_storage_client = Azure()
    azure_object_storage_client.create_client(azure_connection_string=AZURE_CONNECTION_STRING)
    # retrieve original image from container
    original_image_path = "/tmp/" + str(blob)
    azure_object_storage_client.retrieve_from_bucket(container, blob)
    s3_client.upload_file(original_image_path, AWS_BUCKET_NAME, blob)
