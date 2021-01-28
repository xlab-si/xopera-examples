# Capability attributes and properties
This is an example for attributes and properties within TOSCA capabilities. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The `service.yaml` within this directory shows an example on how to use attributes and properties within TOSCA 
capabilities so that they can also be exposed and used in Ansible playbooks.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/capability-attributes-properties
(venv) tosca/capability-attributes-properties$ opera deploy service.yaml
[Worker_0]   Deploying my_first_node_0
[Worker_0]   Deployment of my_first_node_0 complete
[Worker_0]   Deploying my_second_node_0
[Worker_0]     Executing create on my_second_node_0
[Worker_0]   Deployment of my_second_node_0 complete

(venv) tosca/capability-attributes-properties$ opera outputs
output_cap_attr:
  description: Capability attribute output
  value: ' some_attribute'
output_cap_prop:
  description: Capability property output
  value: ' some_property'
output_req_attr:
  description: Requirement attribute output
  value: ' some_integer'
output_req_prop:
  description: Requirement property output
  value: ' some_string'
```

