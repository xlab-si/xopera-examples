# A small TOSCA CSAR
Example of an extracted small TOSCA CSAR. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example show a small TOSCA CSAR that focuses on configuring a TOSCA relationship on a TOSCA node and then 
retrieving the relationship outputs. This is a type of a TOSCA CSAR that doesn't contain a separate 
`TOSCA-Metadata/TOSCA-meta` file for metadata but has metadata specified within the TOSCA service template itself, which
may be more convenient for a small TOSCA CSAR. The special thing about this CSAR is also that it uses JSON inputs file
instead of YAML inputs file which also makes it smaller.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd csars/small
# you can also zip all files without inputs.json in csars/small to small.csar
# compressed CSAR can be deployed with: opera deploy -i inputs.json small.csar
(venv) csars/small$ opera deploy -i inputs.json service.yaml
opera deploy -i inputs.json service.yaml
[Worker_0]   Deploying my_workstation_0
[Worker_0]     Executing pre_configure_target on test_node_0--my_workstation_0
[Worker_0]     Executing post_configure_target on test_node_0--my_workstation_0
[Worker_0]   Deployment of my_workstation_0 complete
[Worker_0]   Deploying test_node_0
[Worker_0]     Executing create on test_node_0
[Worker_0]     Executing pre_configure_source on test_node_0--my_workstation_0
[Worker_0]     Executing post_configure_source on test_node_0--my_workstation_0
[Worker_0]   Deployment of test_node_0 complete

(venv) csars/small$ opera outputs
output_node_attribute:
  description: Node attribute output
  value: Node attribute
output_post_configure_source_attribute:
  description: Relationship attribute output
  value: Relationship attribute
output_post_configure_source_input_attribute:
  description: Relationship attribute output
  value: Hey, I am in relationship!
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
  value: Hey, I am in relationship!
output_relationship_property:
  description: Relationship property output
  value: Relationship property
```

