# AWS thumbnail generator with AWS EC2 VM
Deploy thumbnail generator AWS Lambda along with AWS EC2 instance.

## Table of Contents
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

## Description
The example extents the [thumbnail-generator example](../thumbnail-generator), so for more info look there.
The main functionality of this example the ability to create thumbnails from the source image and display them on web. 
Source image must be uploaded into source bucket and then three thumbnails will be created and saved to another bucket. 
The created thumbnails can then be viewed through the browser with the web app that is hosted on AWS.

## Prerequisites
This example requires a Python dev environment. To set everything up run the following commands:

```console
# Initialize virtualenv with Python and install prerequisites
cd aws
python3.6 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install opera
```

Your AWS credentials should be located in `~/.aws/credentials` (you can also use `~/.aws/config`) or you should export
them into `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` environment variables.

You can also install and configure AWS CLI manually.

```console
# Install AWS CLI v2
curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure your account with your aws credentials (access key, secret key, region)
aws configure
```

## Running with xOpera
You can modify values in `inputs.yaml` to set the appropriate params(IPs, auth params, container names etc.).

| Input | Description | Example |
|:-------------|:-------------|:-------------|
| `host_ip` | Host IP address where you will run the service | localhost |
| `region` | AWS region for your resources | eu-central-1 |
| `lambda_role_name` | The name of the new AWS Lambda role | RadonLambda |
| `function_name` | The name of the new AWS Lambda function | image-resize-function |
| `function_alias` | New alias for the function | latest |
| `permission_id` | Id of the permission - a unique statement identifier for lambda policy | lambda_test_permission |
| `bucket_in_name` | Name of the incoming bucket for original images | original |
| `bucket_out_name` | The name of the bucket containing resized images | resized |
| `lambda_runtime` | Runtime of the deployed lambda | python3.6 |
| `lambda_handler` | Function and method with lambda handler | Python example: image_resize.lambda_handler, Java example:package.ClassName::handlerFunction |
| `lambda_timeout` | Function timeout in seconds | 5 |
| `lambda_memory` | Function memory in MB | 128 |
| `ec2_role_name` | The name of the new AWS EC2 role | DemoEC2Role |
| `ssh_key_name` | The name of the new AWS EC2 SSH key | demo-thumbnail-generator-key |
| `ssh_key_file_path` | Path for saving the generated EC2 VM SSH key | /tmp/ssh_key_file |
| `ssh_user` | The name of the SSH user for AWS EC2 VM | ec2-user |
| `security_group` | The name of the new AWS security group for EC2 VM | DemoEC2Role |
| `instance_type` | AWS EC2 instance type | t2.micro |
| `image` | AWS EC2 image | ami-0db9040eb3ab74509 |

You can invoke deployment and xOpera orchestration with the command below. 

```console
(venv) $ cd cloud/aws/thumbnail-generator-with-vm
(venv) cloud/aws/thumbnail-generator-with-vm$ opera deploy -i inputs.yaml service.yaml
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
[Worker_0]   Deploying bucket_notification_0
[Worker_0]     Executing create on bucket_notification_0
[Worker_0]   Deployment of bucket_notification_0 complete
[Worker_0]   Deploying vpc_subnet_0
[Worker_0]     Executing create on vpc_subnet_0
[Worker_0]   Deployment of vpc_subnet_0 complete
[Worker_0]   Deploying ec2_role_0
[Worker_0]     Executing create on ec2_role_0
[Worker_0]   Deployment of ec2_role_0 complete
[Worker_0]   Deploying ec2_keypair_0
[Worker_0]     Executing create on ec2_keypair_0
[Worker_0]   Deployment of ec2_keypair_0 complete
[Worker_0]   Deploying ec2_vm_0
[Worker_0]     Executing create on ec2_vm_0
[Worker_0]   Deployment of ec2_vm_0 complete
[Worker_0]   Deploying ec2_docker_0
[Worker_0]     Executing create on ec2_docker_0
[Worker_0]   Deployment of ec2_docker_0 complete
[Worker_0]   Deploying ec2_web_app_0
[Worker_0]     Executing create on ec2_web_app_0
[Worker_0]   Deployment of ec2_web_app_0 complete
```

The orchestration outputs can be retrieved with:

```console
(venv) cloud/aws/thumbnail-generator-with-vm$ opera outputs
ec2_web_page_address:
  description: Web page address
  value: http://ec2-18-185-126-68.eu-central-1.compute.amazonaws.com
```

You can undeploy the solution with:

```console
(venv) cloud/aws/thumbnail-generator-with-vm$ opera undeploy
[Worker_0]   Undeploying bucket_out_0
[Worker_0]     Executing delete on bucket_out_0
[Worker_0]   Undeployment of bucket_out_0 complete
[Worker_0]   Undeploying bucket_notification_0
[Worker_0]     Executing delete on bucket_notification_0
[Worker_0]   Undeployment of bucket_notification_0 complete
[Worker_0]   Undeploying lambda_0
[Worker_0]     Executing delete on lambda_0
[Worker_0]   Undeployment of lambda_0 complete
[Worker_0]   Undeploying lambda_role_0
[Worker_0]     Executing delete on lambda_role_0
[Worker_0]   Undeployment of lambda_role_0 complete
[Worker_0]   Undeploying bucket_in_0
[Worker_0]     Executing delete on bucket_in_0
[Worker_0]   Undeployment of bucket_in_0 complete
[Worker_0]   Undeploying ec2_docker_0
[Worker_0]   Undeployment of ec2_docker_0 complete
[Worker_0]   Undeploying ec2_web_app_0
[Worker_0]   Undeployment of ec2_web_app_0 complete
[Worker_0]   Undeploying ec2_vm_0
[Worker_0]     Executing delete on ec2_vm_0
[Worker_0]   Undeployment of ec2_vm_0 complete
[Worker_0]   Undeploying vpc_subnet_0
[Worker_0]     Executing delete on vpc_subnet_0
[Worker_0]   Undeployment of vpc_subnet_0 complete
[Worker_0]   Undeploying ec2_role_0
[Worker_0]     Executing delete on ec2_role_0
[Worker_0]   Undeployment of ec2_role_0 complete
[Worker_0]   Undeploying ec2_keypair_0
[Worker_0]     Executing delete on ec2_keypair_0
[Worker_0]   Undeployment of ec2_keypair_0 complete
[Worker_0]   Undeploying my-workstation_0
[Worker_0]   Undeployment of my-workstation_0 complete
```
