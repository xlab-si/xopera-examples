# AWS thumbnail generator with API Gateway
Image resize functionality deployment with xOpera for Amazon Web Services (using AWS API Gateway).

## Table of Contents
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

## Description
The main functionality of image-resize is to create thumbnails from the source image. Source image must be uploaded 
into source bucket and then three thumbnails will be created and saved to another bucket.

The solution includes next deployment modules separated into folders:

| Role | Description |
|:-------------|:-------------|
| **prerequisites** | Installs prerequisite packages |
| **lambda_role** | Creates a new AWS IAM role for AWS Lambda |
| **bucket** | Creates a new AWS S3 bucket |
| **lambda** | Prepares a zipfile with function and deploys it to AWS Lambda |
| **api-gateway** | Sets up API Gateway that can trigger AWS Lambda |

You can modify values in `inputs.yaml` to set the appropriate params(IPs, auth params, container names etc.).

## Prerequisites
This example requires a Python dev environment. To set everything up run the following commands:

```console
# Initialize virtualenv with Python and install prerequisites
cd aws
python3 -m venv .venv && . .venv/bin/activate
pip install --upgrade pip
pip install opera
```

Your AWS credentials should be located in `~/.aws/credentials` (you can also use `~/.aws/config`) or you should export
them into `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` environment variables.

You can also install and configure AWS CLI manually.

```console
# Install AWS CLI
pip install awscli

# Configure your account with your aws credentials (access key, secret key, region)
aws configure
```

## Running with xOpera
If you want to test the solution with AWS API Gateway you should modify values in `inputs.yaml`. The following values 
can be modified:

| Input | Description | Example |
|:-------------|:-------------|:-------------|
| `host_ip` | Host IP address | localhost |
| `region` | AWS region for your resources | eu-central-1 |
| `lambda_role_name` | The name of the new AWS role | RadonLambda |
| `function_name` | The name of the new AWS Lambda function | image-resize-function |
| `function_alias` | New alias for the function | latest |
| `permission_id` | Id of the permission - a unique statement identifier for lambda policy | lambda_test_permission01 |
| `bucket_in_name` | Name of the incoming bucket for original images | bucket |
| `bucket_out_name` | The name of the bucket containing resized images | original |
| `lambda_runtime` | Runtime of the deployed lambda | python3.6 |
| `lambda_handler` | Function and method with lambda handler | Python example: image_resize.lambda_handler, Java example:package.ClassName::handlerFunction |
| `lambda_timeout` | Function timeout in seconds | 5 |
| `lambda_memory` | Function memory in MB | 128 |
| `api_gateway_title` | The name of the new API gateway | MyAPIGateway |
| `api_gateway_resource_uri` | Resource URI to connect to API Gateway | "arn:aws:apigateway:eu-central-1:lambda:path/2015-03-31/functions/arn:aws:lambda:test:826815320240:function:my-function/invocations" |

There is currently a swagger file for creating API Gateway with one POST method that connects to created AWS lambda. To
connect your own resource delete line `api_gateway_resource_uri_override: "arn:aws:apigateway:{{ aws_region }}:lambda:path/2015-03-31/functions/{{ lambda_function_arn }}/invocations"`
in `modules/api_gateway/playbooks/create.yaml` which overrides `api_gateway_resource_uri` variable.

You can invoke the deployment using the command below. 

```console
(venv) $ cd cloud/aws/thumbnail-generator-with-api-gateway
(venv) cloud/aws/thumbnail-generator-with-api-gateway$ opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying prerequisites_0
[Worker_0]     Executing create on prerequisites_0
[Worker_0]   Deployment of prerequisites_0 complete
[Worker_0]   Deploying lambda_role_0
[Worker_0]     Executing create on lambda_role_0
[Worker_0]   Deployment of lambda_role_0 complete
[Worker_0]   Deploying lambda_0
[Worker_0]     Executing create on lambda_0
[Worker_0]   Deployment of lambda_0 complete
[Worker_0]   Deploying bucket_in_0
[Worker_0]     Executing create on bucket_in_0
[Worker_0]   Deployment of bucket_in_0 complete
[Worker_0]   Deploying bucket_out_0
[Worker_0]     Executing create on bucket_out_0
[Worker_0]   Deployment of bucket_out_0 complete
[Worker_0]   Deploying api_gateway_0
[Worker_0]     Executing create on api_gateway_0
[Worker_0]   Deployment of api_gateway_0 complete
```

You can undeploy the solution with:

```console
(venv) cloud/aws/thumbnail-generator-with-api-gateway$ opera undeploy
[Worker_0]   Undeploying bucket_out_0
[Worker_0]     Executing delete on bucket_out_0
[Worker_0]   Undeployment of bucket_out_0 complete
[Worker_0]   Undeploying api_gateway_0
[Worker_0]     Executing delete on api_gateway_0
[Worker_0]   Undeployment of api_gateway_0 complete
[Worker_0]   Undeploying lambda_0
[Worker_0]     Executing delete on lambda_0
[Worker_0]   Undeployment of lambda_0 complete
[Worker_0]   Undeploying lambda_role_0
[Worker_0]     Executing delete on lambda_role_0
[Worker_0]   Undeployment of lambda_role_0 complete
[Worker_0]   Undeploying bucket_in_0
[Worker_0]     Executing delete on bucket_in_0
[Worker_0]   Undeployment of bucket_in_0 complete
[Worker_0]   Undeploying prerequisites_0
[Worker_0]     Executing delete on prerequisites_0
[Worker_0]   Undeployment of prerequisites_0 complete
[Worker_0]   Undeploying my-workstation_0
[Worker_0]   Undeployment of my-workstation_0 complete
```

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
