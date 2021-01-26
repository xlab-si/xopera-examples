from minio import Minio


class MinIO:
    def __init__(self):
        self.client = None

    def create_client(self, *args, **kwargs):
        ip = kwargs.get('ip', "localhost")
        access_key = kwargs.get('access_key', None)
        secret_key = kwargs.get('secret_key', None)
        self.client = Minio(ip + ':9000',
                            access_key=access_key,
                            secret_key=secret_key,
                            secure=False)

    def retrieve_from_bucket(self, source_bucket, file_name):
        try:
            self.client.fget_object(source_bucket, file_name, "/tmp/" + file_name)
        except Exception as e:
            raise Exception("There was an error retrieving object from the bucket: " + str(e))

    def store_to_bucket(self, destination_bucket, file_name, img_path):
        try:
            self.client.fput_object(destination_bucket, file_name, img_path)
        except Exception as e:
            raise Exception("There was an error storing object to the bucket: " + str(e))
