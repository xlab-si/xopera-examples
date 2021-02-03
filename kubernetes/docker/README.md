# Docker deployment
Install Docker and run a Docker container on a target machine.

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

## Description
The main functionality of this solution is to install Docker service on a target machine and deploy a MinIO Docker 
container on a target machine. [MinIO](https://min.io/) is a high performance, Kubernetes-native object storage suite.
Here MinIO object storage is fully set up and prepared for storing files in the created bucket. After the deployment
you will be able to access MinIO dashboard on `localhost:9000` where you can login wit the credentials you specified 
in `inputs.yaml`.

There are 2 main Ansible playbooks separated into folders. Usage is explained in the table below:

|    Role      |   Purpose    |
|:-------------|:-------------|
| **docker** | Installs docker on a target VM |
| **minio** | Sets up MinIO object storage for files and creates buckets |

You can modify values of variables stored in `inputs.yaml` to set the suitable parameters. The file with inputs is 
later passed to xOpera at the beginning of the orchestration. The inputs are explained in a table below.

| Input | Description | Example
|:-------------|:-------------|:-------------|
| `host_ip` | IP address of your target (virtual) machine | localhost |
| `linux_distro` | Linux distribution of your VM | ubuntu |
| `linux_release` | Linux release of your VM  | bionic |
| `minio_credentials` | MinIO credentials in a map with access and secret key | { access_key: test, secret_key: test } |

### Running with xOpera
When running Ansible playbooks with xOpera on a VM you should specify the username that will be used to connect to
the virtual machine by ssh. This can be done by setting the environment variable `OPERA_SSH_USER`.
You can also skip `OPERA_SSH_USER` when running xOpera by exporting this variable using: `export OPERA_SSH_USER=root`.

You can invoke deployment and xOpera orchestration with the command below. 

```console
(venv) $ cd kubernetes/docker
(venv) kubernetes/docker$ opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying docker_0
[Worker_0]     Executing create on docker_0
[Worker_0]   Deployment of docker_0 complete
[Worker_0]   Deploying minio_0
[Worker_0]     Executing create on minio_0
[Worker_0]   Deployment of minio_0 complete
```

You can undeploy the solution with:

```console
(venv) kubernetes/docker$ opera undeploy
[Worker_0]   Undeploying docker_0
[Worker_0]   Undeployment of docker_0 complete
[Worker_0]     Executing delete on docker_0
[Worker_0]   Undeploying minio_0
[Worker_0]   Undeployment of minio_0 complete
[Worker_0]     Executing delete on minio_0
[Worker_0]   Undeploying my-workstation_0
```
