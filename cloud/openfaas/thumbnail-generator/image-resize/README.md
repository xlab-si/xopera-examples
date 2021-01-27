# xOpera deploy of thumbnail generator (with OpenFaaS and MinIO)

## Table of Contents
  - [Quick test and deploy](#quick-test-and-deploy)
  - [Prerequisites](#prerequisites)
  - [Roles](#roles)
  - [Deploying with xOpera](#deploying-with-xopera)
      - [Building docker images and preparing tar files](#building-docker-images-and-preparing-tar-files)
        - [Editing the function](#editing-the-function)
      - [Credentials](#credentials)
      - [Setting variables](#setting-variables)
      - [Running with xOpera](#running-with-xopera)

## Quick test and deploy
If you want to test this solution immediately run the following commands:

```console
# Install necessary prerequisites
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install git+https://github.com/ansible/ansible.git@devel
pip install opera

# configure MinIO credentials (here we use default example access and secret key)
echo '{ "minio_access_key": "AKIAIOSFODNN7EXAMPLE", "minio_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" }' > /tmp/credentials.json

# Modify vars in inputs.yaml and run ansible playbook build.yaml it to build and pack docker image with image-resize function (or use prepared tar in examples)
cd docker-image-templates
ansible-playbook build.yaml 

# Run deployment with with xOpera (here you should prepare a new VM on OpenStack and configure it to use passwordless ssh)
OPERA_SSH_USER=root opera deploy -i inputs.yaml service.yaml
```

## Prerequisites
You should also prepare virtual machine in OpenStack and configure it to use passwordless ssh. On this VM you
have to setup OpenFaaS and MinIO to be able to run the deployment of image-resize.

To be able to run these roles you should use virtual environment and install the latest Ansible `devel` version.

```console
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install git+https://github.com/ansible/ansible.git@devel
```

Next, you can install opera orchestrator to your virtual environment from [here](https://github.com/xlab-si/xopera-opera).
Basically you need to install it using `pip install opera`.

## Roles
There are 4 playbooks separated into folders. Their usage is explained in the table below:

| Role | Purpose
|:-------------|:-------------|
| **function-load** | loads the given docker image to machine
| **function-deploy** | deploys docker image to OpenFaaS as a function
| **bucket-create** | creates necessary buckets on MinIO server
| **bucket-notification** | creates notification on bucket and configures MinIO server configuration

## Deploying with xOpera
This part describes how to deploy function to OpenFaaS and how to setup simple MinIO object storage along with bucket
notification.

### Building docker images and preparing tar files
Docker images are used for deployment of OpenFaaS functions. Currently one can build one docker image which is a source for
function that gets deployed to OpenFaaS later on. It carries the main functionality of this repository and that is image-resize option 
that creates thumbnails from the source image. Source image must be uploaded into (minIO bucket) and then three thumbnails will be created and saved to another bucket.

An example of tar is in `docker-image-templates` folder.

To prepare tar file with docker image you should run Ansible playbook with:

```console
cd docker-image-templates
ansible-playbook build.yaml 
```

The playbook uses variables from `inputs.yaml` so modify this file according to your system settings.
There is an example of tar file that should be built by ansible-playbook located in `docker-image-templates/examples/python-docker-function.tar`.

#### Editing the function
You can change the functionality on the function by editing `handler.py` located in `thumbnail-deploy-xopera\docker-image-templates\python-function-template\handler.py`.
This prepared function also uses MinIO class located in file `thumbnail-deploy-xopera\docker-image-templates\python-function-template\minio_handler.py`.
There is also an example of JSON message sent to function by MinIO notification trigger in `docker-image-templates/examples/minio_notification_message_example.rst` file.

### Credentials
Create file credentials.json and replace `<my_minio_access_key>` and `<my_minio_secret_key>` with your own MinIO credentials:

```json
{
"minio_access_key":"<my_minio_access_key>", 
"minio_secret_key":"<my_minio_secret_key>"
}
```

Then move your credentials to `/tmp/` folder with `mv credentials.json /tmp/`

### Setting variables
Deployment with xOpera uses inputs that are specified in key-value form in `inputs.yaml` file. You can modify these values
according to yourself to set the appropriate params(IPs, bucket names etc.). The following values can be modified:

| Variable | Purpose | Example
|:-------------|:-------------|:-------------|
| `host_ip` | IP address of your virtual machine (you can use OpenStack floating IP) | 10.10.43.213 |
| `credentials` | MiniIO credentials json file | (move your credentials.json to /tmp/ folder) |
| `bucket_in_name` | The name of incoming the bucket | original |
| `bucket_out_name` | The name of the bucket with results | resized |
| `resize_image_name` | Name of already existing image for image-resize (Image name picked when saving the image has to be the same as actual name of image being saved) | python-docker-test |
| `resize_function_name` | Name of the new OpenFaaS function with image-resize functionality | var-function-name |

### Running with xOpera
When running Ansible playbooks with xOpera you should specify the username that will be used to connect to
the virtual machine by ssh. This can be done by setting the environment variable `OPERA_SSH_USER`.
You can initiate deployment by running: `OPERA_SSH_USER=root opera deploy -i inputs.yaml service.yaml`
You can also skip `OPERA_SSH_USER` when running xOpera by exporting this variable using: `export OPERA_SSH_USER=root`.
If you wish to undeploy your solution you can run: `OPERA_SSH_USER=root opera undeploy`
