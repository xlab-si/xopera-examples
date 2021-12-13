# OpenStack and nginx
An example of OpenStack and nginx deployment. 

## Table of Contents
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

## Description
This example shows how to deploy and set up an OpenStack VM and an nginx site on top of it.

After the deployment the sample HTML website will be available on `<YOUR_VM_IP>:80`, so make sure that you unlock the
(ingress) port `80` within the specified OpenStack security group.

## Prerequisites
To run this example we need some prerequisites such as running OpenStack.
Because using OpenStack modules from Ansible playbooks is quite common,
we can install `opera` with all required OpenStack libraries by running:

```console
(.venv) $ pip install -U opera[openstack]
```

Before we can actually use the OpenStack functionality, we also need to
obtain the OpenStack credentials. If we log into OpenStack and navigate
to the `Access & Security` -\> `API Access` page, we can download the rc
file with all required information.

At the start of each session (e.g., when we open a new command line
console), we must source the rc file by running:

```console
(venv) $ . openstack.rc
```

After we enter the password, we are ready to start using the OpenStack
modules in playbooks that implement life cycle operations.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd misc/nginx-openstack
(venv) misc/nginx-openstack$ opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying vm_0
[Worker_0]     Executing create on vm_0
[Worker_0]   Deployment of vm_0 complete
[Worker_0]   Deploying nginx_0
[Worker_0]     Executing create on nginx_0
[Worker_0]     Executing post_configure_target on site_0--nginx_0
[Worker_0]   Deployment of nginx_0 complete
[Worker_0]   Deploying site_0
[Worker_0]     Executing create on site_0
[Worker_0]   Deployment of site_0 complete
```

You can undeploy the solution with:

```console
(venv) misc/nginx-openstack$ opera undeploy
[Worker_0]   Undeploying site_0
[Worker_0]     Executing delete on site_0
[Worker_0]   Undeployment of site_0 complete
[Worker_0]   Undeploying nginx_0
[Worker_0]     Executing delete on nginx_0
[Worker_0]   Undeployment of nginx_0 complete
[Worker_0]   Undeploying vm_0
[Worker_0]     Executing delete on vm_0
[Worker_0]   Undeployment of vm_0 complete
```
