# Relationship outputs
Example with TOSCA relationship outputs. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows how to retrieve orchestration outputs from TOSCA relationships and how to use them within Ansible
playbooks.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/relationship-outputs
(venv) tosca/relationship-outputs$ opera deploy service.yaml
[Worker_0]   Deploying my_workstation_0
[Worker_0]     Executing pre_configure_target on test_node_0--my_workstation_0
[Worker_0]     Executing post_configure_target on test_node_0--my_workstation_0
[Worker_0]   Deployment of my_workstation_0 complete
[Worker_0]   Deploying test_node_0
[Worker_0]     Executing create on test_node_0
[Worker_0]     Executing pre_configure_source on test_node_0--my_workstation_0
[Worker_0]     Executing post_configure_source on test_node_0--my_workstation_0
[Worker_0]   Deployment of test_node_0 complete

(venv) tosca/relationship-outputs$ opera outputs
output_node_attribute:
  description: Node attribute output
  value: Node attribute
output_post_configure_source_attribute:
  description: Relationship attribute output
  value: Relationship attribute
output_post_configure_source_input_attribute:
  description: Relationship attribute output
  value: Relationship input
output_post_configure_source_property_attribute:
  description: Relationship attribute output
  value: Relationship property
output_post_configure_source_txt_file_attribute:
  description: Relationship attribute output
  value: This is an example file content.
output_post_configure_target_attribute:
  description: Relationship attribute output
  value: This is post configure target attribute
output_pre_configure_source_attribute:
  description: Relationship attribute output
  value: This is pre configure source attribute
output_pre_configure_target_attribute:
  description: Relationship attribute output
  value: This is pre configure target attribute
output_relationship_attribute:
  description: Relationship attribute output
  value: Relationship attribute
output_relationship_input:
  description: Relationship input output
  value: Relationship input
output_relationship_property:
  description: Relationship property output
  value: Relationship property
```

