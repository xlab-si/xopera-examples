# Intrinsic functions
This is an example for TOSCA intrinsic functions. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows the usage of TOSCA intrinsic functions within TOSCA template where the results of these functions
can be then retrieved as orchestration outputs.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/intrinsic-functions
(venv) tosca/intrinsic-functions$ opera deploy service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying hello1_0
[Worker_0]   Deployment of hello1_0 complete
[Worker_0]   Deploying hello2_0
[Worker_0]   Deployment of hello2_0 complete
[Worker_0]   Deploying hello3_0
[Worker_0]   Deployment of hello3_0 complete

(venv) tosca/intrinsic-functions$ opera outputs
attribute:
  description: Attribute value
  value: 'Attribute: property'
concat_output:
  description: Concatenate string values
  value: http://attribute1:property1
join1_output:
  description: Join string values without a delimiter (concat)
  value: tosca
join2_output:
  description: Join string values with delimiter
  value: t_o_s_c_a
join3_output:
  description: Join string values with delimiter
  value: input, attribute2, property2
properties:
  description: Joined properties
  value: 'Properties: property1 property2 property'
property:
  description: Property value
  value: 'Property: attribute'
token1_output:
  description: Tokenize the string and get the zeroth substring
  value: '111'
token2_output:
  description: Tokenize the string and get the second substring
  value: s
```

