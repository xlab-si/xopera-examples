# xOpera deploy of simple thumbnail generator on GCP with Ansible

## Table of Contents
  - [Purpose](#purpose)
  - [Functionality](#functionality)
  - [Quick test and deploy](#quick-test-and-deploy)
  - [Deployment instructions](#deployment-instructions)
      - [Prerequisites](#prerequisites)
      - [Roles and deployment](#roles-and-deployment)
      - [Setting inputs](#setting-inputs)
      - [Python function for resizing images](#python-function-for-resizing-images)
      - [Running with xOpera](#running-with-xopera)

## Purpose
The repository implements image resize functionality deployment with xOpera for Google Cloud Platform.

## Functionality
The main functionality of image-resize is to create thumbnails from the source image. Source image must be uploaded 
into source bucket and then three thumbnails will be created and saved to another bucket.

## Quick test and deploy
If you want to test this solution immediately run the following commands:

```console
# install Google Cloud SDK from https://cloud.google.com/sdk/docs/downloads-apt-get
# with apt-get:
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get install apt-transport-https ca-certificates gnupg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-sdk

# Create GCP service account, create a JSON file key and put to /tmp folder
cat /tmp/service_account.json

# install prerequisites
cd gcp
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install opera

# run xOpera service (don't forget to set the appropriate inputs in inputs.yaml)
opera deploy -i inputs.yaml service.yaml
```

## Deployment instructions
The next part explains the deployment of this solution in detail.

### Prerequisites
This topic explains prerequisites to run xOpera deploy via GCP. If you want to test it immediately go to 
[quick test](#quick-test-and-deploy)

Firstly you will have to install [Google Cloud SDK](https://cloud.google.com/sdk/install) in order to operate
with GCP resources.

To be able to run these roles you should use virtual environment and install the latest Ansible version which is already
included as a dependency of opera TOSCA orchestrator. You can install opera orchestrator to your virtual environment 
from [here](https://github.com/xlab-si/xopera-opera).

```console
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install opera
```

The next thing is to create a Google Cloud Service Account (navigate to IAM) and then set permissions to access Google
Storage from this account. After that you can generate a new key along with a JSON file that can be downloaded. For the
security reasons you can put it to `/tmp` folder and access it by setting the `service_account_file` TOSCA input.

### Roles and deployment
We use the Ansible playbooks to call TOSCA operations that are separated into following folders:

| Role | Purpose
|:-------------|:-------------|
| **bucket** | Creates GCP storage buckets |
| **function** | Deploys GCP function |

### Setting inputs
You can modify values of variables stored in `inputs.yaml` to set the suitable parameters like IPs, bucket names, paths 
etc. Currently the following values can be modified:

| Inout (variable) | Description | Example
|:-------------|:-------------|:-------------|
| `host_ip` | IP address of your target machine for execution | localhost |
| `project_id` | Project ID = a unique, user-assigned ID that can be used by Google APIs | project-123456 |
| `service_account_file` | Location of the service account JSON file | /tmp/service_account.json |
| `bucket_location` | Location for the created buckets (GCP region) | EU |
| `bucket_in_name` | The name of the incoming GCP bucket | radon-original |
| `bucket_out_name` | The name of the GCP bucket with results | radon-resized |
| `bucket_function_name` | The name of the GCP bucket with function zip archive | radon-function |
| `function_name` | Name of the new GCP function | image-resize |
| `function_runtime` | The runtime environment where function will run | python37 |
| `function_entry_point` | The name of function from the source code to call when the GCP function is triggered | entry_point |
| `function_timeout` | Function timeout in seconds | 60s |
| `function_memory` | Function memory in MB | 256 |

The file with inputs is later passed to xOpera at the beginning of the orchestration.

### Python function for resizing images
In this example we use a Python function for resizing images.
The function takes the original image from original bucket and creates three thumbnails (look for `THUMBNAIL_SIZES_PX` 
in [python code](./modules/function/playbooks/function/main.py)) which are then stored to the bucket with results.

## Running with xOpera
You can run xOpera resize service with `opera deploy -i inputs.yaml service.yaml`
To un-deploy the solution run `opera undeploy`
