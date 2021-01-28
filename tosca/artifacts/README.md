# Artifacts
This is a TOSCA artifacts example. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The `service.yaml` within this directory shows a service template that uses TOSCA artifacts and `get_artifact`
TOSCA function. Moreover, there is a node type that accepts JSON and text file artifact inputs and exposes them
to Ansible playbooks were their content is explored.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/artifacts
(venv) tosca/artifacts$ opera deploy service.yaml
[Worker_0]   Deploying artifacts_file_0
[Worker_0]     Executing create on artifacts_file_0
[Worker_0]   Deployment of artifacts_file_0 complete

(venv) tosca/artifacts$ opera outputs
output_attribute_json_file:
  description: Example of attribute output
  value:
    content: This is an example JSON file content.
output_attribute_text_file:
  description: Example of attribute output
  value: This is an example file content.
```

