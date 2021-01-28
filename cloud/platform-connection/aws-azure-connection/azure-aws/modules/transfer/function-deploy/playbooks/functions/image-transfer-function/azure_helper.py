from azure.storage.blob import BlockBlobService


class Azure:
    def __init__(self):
        self.client = None

    def create_client(self, azure_connection_string):
        self.client = BlockBlobService(connection_string=azure_connection_string)

    def retrieve_from_bucket(self, source_bucket, file_name):
        try:
            self.client.get_blob_to_path(source_bucket, file_name, "/tmp/" + file_name)
        except Exception as e:
            raise Exception("There was an error retrieving object from the bucket: " + str(e))

    def store_to_bucket(self, destination_bucket, file_name, img_path):
        try:
            self.client.create_blob_from_path(destination_bucket, file_name, img_path)
        except Exception as e:
            raise Exception("There was an error storing object to the bucket: " + str(e))
