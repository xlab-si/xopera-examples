# OpenStack and nginx
An example of OpenStack and nginx deployment. 

## Table of Contents
  - [Description](#description)
    - [Prerequisites](#prerequisites)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows how to deploy and set up an OpenStack VM and the an nginx site on top of it.

## Prerequisites
To run this example we need some prerequisites such as running OpenStack.
Because using OpenStack modules from Ansible playbooks is quite common,
we can install `opera` with all required OpenStack libraries by running:

    (.venv) $ pip install -U opera[openstack]

Before we can actually use the OpenStack functionality, we also need to
obtain the OpenStack credentials. If we log into OpenStack and navigate
to the `Access & Security` -\> `API Access` page, we can download the rc
file with all required information.

At the start of each session (e.g., when we open a new command line
console), we must source the rc file by running:

    (venv) $ . openstack.rc

After we enter the password, we are ready to start using the OpenStack
modules in playbooks that implement life cycle operations.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd misc/nginx-openstack
(venv) misc/nginx-openstack$ opera deploy service.yaml
```

