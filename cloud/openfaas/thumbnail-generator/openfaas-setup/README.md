# System, MinIO and OpenFaaS setup

## Table of Contents
  - [Quick test and deploy](#quick-test-and-deploy)
  - [Prerequisites and system installations](#prerequisites-and-system-installations)
  - [Roles](#roles)
  - [Deploying with xOpera](#deploying-with-xopera)
    - [Credentials](#credentials)
    - [Setting variables](#setting-variables-as-inputs)
    - [Running with xOpera](#running-with-xopera)
  
## Quick test and deploy
If you want to test this solution immediately run the following commands:

```console
# Install necessary prerequisites
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install ansible
pip install opera

# configure MinIO credentials (here we use default example access and secret key)
echo '{ "minio_access_key": "AKIAIOSFODNN7EXAMPLE", "minio_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" }' > /tmp/credentials.json

# Run deployment with with xOpera (here you should prepare a new VM on OpenStack and configure it to use passwordless ssh and modify inputs.yaml)
OPERA_SSH_USER=root opera deploy -i inputs.yaml service.yaml
```

## Prerequisites and system installations
To be able to run these roles you should use virtual environment and install the latest Ansible `devel` version.

```console
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install git+https://github.com/ansible/ansible.git@devel
```

Next, you can install opera orchestrator to your virtual environment from [here](https://github.com/xlab-si/xopera-opera).
Basically you need to install it using `pip install opera`.

You should also prepare virtual machine in OpenStack and configure it to use passwordless ssh.

## Roles
There are 3 playbooks separated into folders. Their usage is explained in the table below:

| Role | Purpose
|:-------------|:-------------|
| **docker** | installs docker on a target machine
| **openfaas** | sets up OpenFaaS on a VM
| **minio** | sets up MinIO object storage and creates buckets

## Deploying with xOpera
This part describes how to deploy function to OpenFaaS and how to setup simple MinIO object storage along with bucket
notification.

### Credentials
Create file credentials.json and replace `<my_minio_access_key>` and `<my_minio_secret_key>` with your own MinIO 
credentials:

```json
{
   "minio_access_key": "<my_minio_access_key>",
   "minio_secret_key": "<my_minio_secret_key>"
}
```

Then move your credentials to `/tmp/` folder with: `mv credentials.json /tmp/`

### Setting variables as inputs
You can modify values in `inputs.yaml` to set the appropriate params(IPs, bucket names, etc.). The following values can 
be modified:

| Variable | Purpose | Example
|:-------------|:-------------|:-------------|
| `host_ip` | IP address of your virtual machine (you can use OpenStack floating IP) | 10.10.43.213 |
| `credentials` | MiniIO credentials json file | (move your credentials.json to /tmp/ folder)  |
| `linux_distro` | Name of linux distribution | ubuntu |
| `linux_release` | Name of linux release | bionic |

### Running with xOpera
When running Ansible playbooks with xOpera you should specify the username that will be used to connect to
the virtual machine by ssh. This can be done by setting the environment variable `OPERA_SSH_USER`.
You can start the deployment by running: `OPERA_SSH_USER=root opera deploy -i inputs.yaml service.yaml`
You can also skip `OPERA_SSH_USER` when running xOpera by exporting this variable using: `export OPERA_SSH_USER=root`.
