# AWS S3 bucket
AWS S3 bucket deployment with xOpera and experimental [TOSCA Version 2.0](https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.html).

## Table of Contents
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

## Description
The main functionality of this example is the deployment of AWS S3 bucket.

The solution includes next deployment modules separated into folders:

| Role | Description |
|:-------------|:-------------|
| **prerequisites** | Installs prerequisite packages |
| **bucket** | Creates a new AWS S3 bucket |

You can modify values in `inputs.yaml` to set the appropriate params (IPs, auth params, container names etc.).

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
You can modify values in `inputs.yaml` to set the appropriate params(IPs, auth params, container names etc.).

| Input | Description | Example |
|:-------------|:-------------|:-------------|
| `host_ip` | Host IP address | localhost |
| `region` | AWS region for your resources | eu-central-1 |
| `bucket_name` | The name of the S3 bucket| my-bucket |

You can invoke the validation, deployment and undeployment using the commands below.

```console
(.venv) $ cd cloud/aws/s3-bucket
(.venv) cloud/aws/s3-bucket$ opera validate -i inputs.yaml service.yaml
Validating TOSCA CSAR or service template...
Done.

(.venv) cloud/aws/s3-bucket$ opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying prerequisites_0
[Worker_0]     Executing create on prerequisites_0
[Worker_0]   Deployment of prerequisites_0 complete
[Worker_0]   Deploying bucket_0
[Worker_0]     Executing create on bucket_0
[Worker_0]   Deployment of bucket_0 complete

(.venv) cloud/aws/s3-bucket$ opera undeploy
[Worker_0]   Undeploying bucket_0
[Worker_0]     Executing delete on bucket_0
[Worker_0]   Undeployment of bucket_0 complete
[Worker_0]   Undeploying prerequisites_0
[Worker_0]     Executing delete on prerequisites_0
[Worker_0]   Undeployment of prerequisites_0 complete
[Worker_0]   Undeploying my-workstation_0
[Worker_0]   Undeployment of my-workstation_0 complete
```
