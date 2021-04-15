# Kubernetes with Rancher
Run Kubernetes with a [Rancher](https://rancher.com/) Docker container.

## Table of Contents
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

## Prerequisites
Minimum requirements for running Kubernetes with Rancher are:

* Operating Systems:
  * Ubuntu 16.04 (64-bit)
  * Red Hat Enterprise Linux 7.5 (64-bit)
  * RancherOS 1.4 (64-bit)
* Hardware:
  * 4 GB of Memory
* Software:
  * Docker Engine v1.12.6, 1.13.1, 17.03.2

To install Docker on your machine you can use our [Docker xOpera example](../docker).

## Description
The main functionality of this solution is to run a Kubernetes service in a Rancher Docker container on a target 
machine. The deployed Kubernetes dashboard is the available on `localhost:80` and `localhost:443`. Additionally we 
deploy the [Prometheus helm chart](https://artifacthub.io/packages/helm/prometheus-community/prometheus) to be able to 
monitor the Kubernetes cluster.

There are 2 main Ansible playbooks separated into folders. Usage is explained in the table below:

|    Role      |   Purpose    |
|:-------------|:-------------|
| **rancher** | Installs Kubernetes by running Rancher Docker container |
| **prometheus-helm-chart** | Sets up cluster monitoring with Prometheus helm chart |

You can modify values of variables stored in `inputs.yaml` to set the suitable parameters. The file with inputs is 
later passed to xOpera at the beginning of the orchestration. The inputs are explained in a table below.

| Input | Description | Example
|:-------------|:-------------|:-------------|
| `host_ip` | IP address of your target (virtual) machine | localhost |

### Running with xOpera
You can invoke deployment and xOpera orchestration with the command below. 

```console
(venv) $ cd kubernetes/rancher
(venv) kubernetes/rancher opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying rancher_0
[Worker_0]     Executing create on rancher_0
[Worker_0]   Deployment of rancher_0 complete
[Worker_0]   Deploying prometheus-helm-chart_0
[Worker_0]     Executing create on prometheus-helm-chart_0
[Worker_0]   Deployment of prometheus-helm-chart_0 complete
```

You can undeploy the solution with:

```console
(venv) kubernetes/rancher$ opera undeploy
[Worker_0]   Undeploying prometheus-helm-chart_0
[Worker_0]     Executing delete on prometheus-helm-chart_0
[Worker_0]   Undeployment of prometheus-helm-chart_0 complete
[Worker_0]   Undeploying rancher_0
[Worker_0]     Executing delete on rancher_0
[Worker_0]   Undeployment of rancher_0 complete
[Worker_0]   Undeploying my-workstation_0
[Worker_0]   Undeployment of my-workstation_0 complete
```
