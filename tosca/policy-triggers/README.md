# Policies and triggers
This is an example with TOSCA policies and triggers. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The `service.yaml` within this example shows an example of TOSCA policies and TOSCA triggers. This example is 
currently meant just for parsing these entities since opera cannot do anything with them for now.

# Running with xOpera
We can run our hello-world as follows:

```console
(venv) $ cd misc/policy-triggers
(venv) policy-triggers$ opera deploy service.yaml
[Worker_0]   Deploying workstation_0
[Worker_0]   Deployment of workstation_0 complete
[Worker_0]   Deploying openstack_vm_0
[Worker_0]     Executing create on openstack_vm_0
[Worker_0]   Deployment of openstack_vm_0 complete
```
