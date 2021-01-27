# xOpera deploy of simple thumbnail generator to AWS with Ansible

## Table of Contents
  - [Purpose](#purpose)
  - [Functionality](#functionality)
  - [Quick test and deploy](#quick-test-and-deploy)
  - [Prerequisites](#prerequisites)
  - [Roles and deployment](#roles-and-deployment)
  - [Setting inputs](#setting-inputs)
    - [Setting inputs for default solution](#inputs-for-the-default-solution)
    - [API Gateway inputs](#api-gateway-inputs)
  - [Running with xOpera](#running-with-xopera)
    - [API Gateway deployment](#api-gateway)
        - [Testing the API Gateway](#testing-the-api-gateway)

## Purpose
The repository implements image resize functionality deployment with xOpera for Amazon Web Services.

## Functionality
The main functionality of image-resize is to create thumbnails from the source image. Source image must be uploaded into
source bucket and then three thumbnails will be created and saved to another bucket.

## Quick test and deploy
If you want to test this solution immediately run the following commands:

```console
# Install AWS CLI v2
curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure your account with your aws credentials (access key, secret key, region)
aws configure

# Initialize virtualenv with Python 3.6 and install prerequisites
cd aws
python3.6 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install ansible
pip install opera

# Run xOpera service (make sure to setup inputs in inputs.yaml)
opera deploy -i inputs.yaml resize_service_opera_v1_3.yaml

# You can also run the following command to undeploy the solution:
opera undeploy

# If you want to test the API Gateway solution run (make sure to modify inputs in inputs-api.yaml):
opera deploy -i inputs-api-gateway.yaml service-api-gateway.yaml
```

Python 3.6 is required! If you don't have it try to follow this answer: https://stackoverflow.com/questions/55773634/how-to-install-python-3-6-on-ubuntu-19-04

## Prerequisites
This topic explains prerequisites to run xOpera deploy via AWS. If you want to test it immediately go to [quick test section](#quick-test-and-deploy)

To be able to run these roles you should use virtual environment with Python 3.6 (there are some issues with Python 3.7)
and install the latest Ansible version.

```console
python3.6 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install ansible
```

## Roles and deployment
There are 5 playbooks separated into folders. Usage is explained in the table below:

| Role | Description |
|:-------------|:-------------|
| **aws_role** | Creates a new AWS role |
| **bucket** | Creates a new AWS S3 bucket |
| **lambda** | Prepares a zipfile with function and deploys it to AWS Lambda |
| **bucket-notification** | Creates bucket notification for triggering the lambda |
| **api-gateway** | Prepares Swagger yaml file and deploys a new API Gateway |

## Setting inputs
This part explains variable setup for the solution.

### Inputs for the default solution
You can modify values in `inputs.yaml` to set the appropriate params(IPs, auth params, container names etc.).

| Input | Description | Example |
|:-------------|:-------------|:-------------|
| `host_ip` | Host IP address | localhost |
| `aws_region` | Your AWS region for your resources | eu-central-1 |
| `role_name` | The name of the new AWS role | RadonLambda |
| `role_description` | AWS role description | Lambda role |
| `function_name` | The name of the new AWS Lambda function | image-resize-function |
| `function_alias` | New alias for the function | latest |
| `permission_id` | Id of the permission - a unique statement identifier for lambda policy | lambda_test_permission |
| `bucket_in_name` | Name of the incoming bucket for original images | original |
| `bucket_out_name` | The name of the bucket containing resized images | resized |
| `lambda_runtime` | Runtime of the deployed lambda | python3.6 |
| `lambda_handler` | Function and method with lambda handler | Python example: image_resize.lambda_handler, Java example:package.ClassName::handlerFunction |
| `lambda_timeout` | Function timeout in seconds | 5 |
| `lambda_memory` | Function memory in MB | 128 |

### API Gateway inputs
If you want to test the solution with AWS API Gateway you should modify values in `inputs-api.yaml`. The following values can be modified:

There is currently a swagger file for creating API Gateway with one POST method that connects to created AWS lambda. To
connect your own resource delete line `api_gateway_resource_uri_override: "arn:aws:apigateway:{{ aws_region }}:lambda:path/2015-03-31/functions/{{ lambda_function_arn }}/invocations"`
in `modules/api_gateway/playbooks/create.yaml` which overrides `api_gateway_resource_uri` variable.

| Input | Description | Example |
|:-------------|:-------------|:-------------|
| `host_ip` | Host IP address | localhost |
| `aws_region` | Your AWS region for your resources | eu-central-1 |
| `role_name` | The name of the new AWS role | RadonLambda |
| `role_description` | AWS role description | Lambda role |
| `function_name` | The name of the new AWS Lambda function | image-resize-function |
| `function_alias` | New alias for the function | latest |
| `permission_id` | Id of the permission - a unique statement identifier for lambda policy | lambda_test_permission01 |
| `bucket_in_name` | Name of the incoming bucket for original images | bucket |
| `bucket_out_name` | The name of the bucket containing resized images | original |
| `api_gateway_title` | The name of the new API gateway | MyAPIGateway |
| `api_gateway_resource_uri` | Resource URI to connect to API Gateway | "arn:aws:apigateway:eu-central-1:lambda:path/2015-03-31/functions/arn:aws:lambda:test:826815320240:function:my-function/invocations" |
| `lambda_runtime` | Runtime of the deployed lambda | python3.6 |
| `lambda_handler` | Function and method with lambda handler | Python example: image_resize.lambda_handler, Java example:package.ClassName::handlerFunction |
| `lambda_timeout` | Function timeout in seconds | 5 |
| `lambda_memory` | Function memory in MB | 128 |

## Running with xOpera
You can run xOpera resize service with `opera deploy -i inputs.yaml service.yaml` 
Run `opera undeploy` to un-deploy the solution.

### API Gateway
There is also an additional TOSCA artifact example using AWS API Gateway.
You can run xOpera resize service with `opera deploy -i inputs-api-gateway.yaml service-api-gateway.yaml`

#### Testing the API Gateway
You can test the deployment of your API Gateway by uploading the image to your original bucket and then invoking the
function in API by testing the POST method. Here you can provide the following request body:

```json
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "bucket-name"
        },
        "object": {
          "key": "image.jpg"
        }
      }
    }
  ]
}
```

You can also try to invoke the API using Postman or curl.
