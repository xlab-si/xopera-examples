from minio import Minio
import requests

node_ip = "{{ node_ip }}"
access_key_minio = "{{ credentials.minio_access_key }}"
secret_key_minio = "{{ credentials.minio_secret_key }}"

mc = Minio(node_ip + ':9000', access_key=access_key_minio, secret_key=secret_key_minio, secure=False)

events = mc.listen_bucket_notification('{{ bucket_in_name }}', '', '.jpg', ['s3:ObjectCreated:*'])

for event in events:
    image = event["Records"][0]["s3"]["object"]["key"]
    data = '{"Records": [{"s3": {"bucket": {"name": "{{ bucket_in_name }}"},"object": {"key":"' + str(image) + '"}}}]}'
    requests.post(url="http://" + node_ip + ":8080/function/{{ function_name }}", data=data)
