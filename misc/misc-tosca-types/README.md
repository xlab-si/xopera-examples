# Misc TOSCA entities
Example of using a lot of different TOSCA entities. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example was first meant just as an integration test and it shows the power of TOSCA through the usage of different
TOSCA entities. The example covers a lot from TOSCA and is therefore appropriate to show what `opera` can currently do.
A special thing about this example is also that it is an extracted version of the TOSCA CSAR with a proper structure so 
that it can be compressed and deployed as a compressed TOSCA CSAR which contains all TOSCA metadata, templates and their
implementations (Ansible playbooks) an all the other accompanying files.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd misc/misc-tosca-types
(venv) misc/misc-tosca-types$ opera deploy -i inputs.yaml service.yaml
[Worker_0]   Deploying my-workstation1_0
[Worker_0]   Deployment of my-workstation1_0 complete
[Worker_0]   Deploying my-workstation2_0
[Worker_0]   Deployment of my-workstation2_0 complete
[Worker_0]   Deploying file_0
[Worker_0]     Executing create on file_0
[Worker_0]   Deployment of file_0 complete
[Worker_0]   Deploying hello_0
[Worker_0]     Executing create on hello_0
[Worker_0]   Deployment of hello_0 complete
[Worker_0]   Deploying interfaces_0
[Worker_0]     Executing create on interfaces_0
[Worker_0]     Executing configure on interfaces_0
[Worker_0]     Executing start on interfaces_0
[Worker_0]   Deployment of interfaces_0 complete
[Worker_0]   Deploying noimpl_0
[Worker_0]   Deployment of noimpl_0 complete
[Worker_0]   Deploying setter_0
[Worker_0]     Executing create on setter_0
[Worker_0]   Deployment of setter_0 complete
[Worker_0]   Deploying test_0
[Worker_0]     Executing create on test_0
[Worker_0]   Deployment of test_0 complete

(venv) misc/misc-tosca-types$ opera outputs
node_output_attr:
  description: Example of attribute output
  value: my_custom_attribute_value
node_output_prop:
  description: Example of property output
  value: 123
relationship_output_attr:
  description: Example of attribute output
  value: rel_attr_test123
relationship_output_prop:
  description: Example of attribute output
  value: rel_prop_test123
```

