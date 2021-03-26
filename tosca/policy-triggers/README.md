# Policies and triggers
This is an example with TOSCA policies and triggers. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The `service.yaml` within this example shows an example of TOSCA policies and TOSCA triggers. This example is 
currently meant to show the possible usage of these entities that can be invoked with `opera notify` CLI command after
the deployment.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/policy-triggers
(venv) tosca/policy-triggers$ opera deploy service.yaml
[Worker_0]   Deploying workstation_0
[Worker_0]   Deployment of workstation_0 complete
[Worker_0]   Deploying openstack_vm_0
[Worker_0]     Executing create on openstack_vm_0
[Worker_0]   Deployment of openstack_vm_0 complete

# invoke TOSCA policy scale down trigger interface operations with opera notify
(venv) tosca/policy-triggers$ opera notify -t radon.triggers.scaling.ScaleDown
[Worker_0]   Notifying workstation_0
[Worker_0]   Notification on workstation_0 complete
[Worker_0]   Notifying openstack_vm_0
[Worker_0]    Calling trigger radon.triggers.scaling.ScaleDown with event scale_down_trigger
[Worker_0]     Executing scale_down on openstack_vm_0
[Worker_0]    Calling trigger actions with event scale_down_trigger complete
[Worker_0]   Notification on openstack_vm_0 complete

# invoke TOSCA policy scale up trigger interface operations with opera notify
(venv) tosca/policy-triggers$ opera notify -t radon.triggers.scaling.ScaleUp
[Worker_0]   Notifying workstation_0
[Worker_0]   Notification on workstation_0 complete
[Worker_0]   Notifying openstack_vm_0
[Worker_0]    Calling trigger radon.triggers.scaling.ScaleUp with event scale_up_trigger
[Worker_0]     Executing scale_up on openstack_vm_0
[Worker_0]    Calling trigger actions with event scale_up_trigger complete
[Worker_0]   Notification on openstack_vm_0 complete

# invoke TOSCA policy auto-scale trigger interface operations with opera notify
(venv) tosca/policy-triggers$ opera notify -t radon.triggers.scaling.AutoScale
[Worker_0]   Notifying workstation_0
[Worker_0]   Notification on workstation_0 complete
[Worker_0]   Notifying openstack_vm_0
[Worker_0]    Calling trigger radon.triggers.scaling.AutoScale with event auto_scale_trigger
[Worker_0]     Executing retrieve_info on openstack_vm_0
[Worker_0]     Executing autoscale on openstack_vm_0
[Worker_0]    Calling trigger actions with event auto_scale_trigger complete
[Worker_0]   Notification on openstack_vm_0 complete

(venv) tosca/policy-triggers$ opera undeploy
[Worker_0]   Undeploying hello_0
[Worker_0]     Executing delete on hello_0
[Worker_0]   Undeployment of hello_0 complete
[Worker_0]   Undeploying my-workstation_0
[Worker_0]   Undeployment of my-workstation_0 complete
```
