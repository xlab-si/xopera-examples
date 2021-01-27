# Outputs
Example with TOSCA outputs. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows how to retrieve orchestration outputs from TOSCA properties and attributes.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/outputs
(venv) tosca/outputs$ opera deploy service.yaml
[Worker_0]   Deploying my_node_0
[Worker_0]     Executing create on my_node_0
[Worker_0]   Deployment of my_node_0 complete

(venv) tosca/outputs$ opera outputs
output_attr:
  description: Example of attribute output
  value: my_custom_attribute_value
output_prop:
  description: Example of property output
  value: 123
```

