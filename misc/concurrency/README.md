# Concurrent execution
Example of concurrent execution with opera. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows the possibility to execute some TOSCA node templates concurrently by specifying the amount of
available workers (execution threads) which results in faster deployment.

# Running with xOpera
We can run this example as follows:

```console
(venv) misc/concurrency$ opera deploy -w 10 service.yaml
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying hello-1_0
[Worker_1]   Deploying hello-2_0
[Worker_0]     Executing create on hello-1_0
[Worker_2]   Deploying hello-3_0
[Worker_4]   Deploying hello-4_0
[Worker_3]   Deploying hello-8_0
[Worker_6]   Deploying hello-9_0
[Worker_1]     Executing create on hello-2_0
[Worker_5]   Deploying hello-10_0
[Worker_6]     Executing create on hello-9_0
[Worker_4]     Executing create on hello-4_0
[Worker_7]   Deploying hello-14_0
[Worker_2]     Executing create on hello-3_0
[Worker_3]     Executing create on hello-8_0
[Worker_5]     Executing create on hello-10_0
[Worker_7]     Executing create on hello-14_0
[Worker_6]     Executing start on hello-9_0
[Worker_2]     Executing start on hello-3_0
[Worker_7]     Executing start on hello-14_0
[Worker_4]     Executing start on hello-4_0
[Worker_5]     Executing start on hello-10_0
[Worker_7]   Deployment of hello-14_0 complete
[Worker_6]   Deployment of hello-9_0 complete
[Worker_2]   Deployment of hello-3_0 complete
[Worker_8]   Deploying hello-12_0
[Worker_8]     Executing create on hello-12_0
[Worker_4]   Deployment of hello-4_0 complete
[Worker_7]   Deploying hello-13_0
[Worker_7]     Executing create on hello-13_0
[Worker_3]     Executing start on hello-8_0
[Worker_1]     Executing start on hello-2_0
[Worker_0]     Executing start on hello-1_0
[Worker_8]     Executing start on hello-12_0
[Worker_5]   Deployment of hello-10_0 complete
[Worker_7]     Executing start on hello-13_0
[Worker_8]   Deployment of hello-12_0 complete
[Worker_3]   Deployment of hello-8_0 complete
[Worker_7]   Deployment of hello-13_0 complete
[Worker_1]   Deployment of hello-2_0 complete
[Worker_0]   Deployment of hello-1_0 complete
[Worker_6]   Deploying hello-5_0
[Worker_2]   Deploying hello-11_0
[Worker_2]     Executing create on hello-11_0
[Worker_6]     Executing create on hello-5_0
[Worker_6]     Executing start on hello-5_0
[Worker_2]     Executing start on hello-11_0
[Worker_6]   Deployment of hello-5_0 complete
[Worker_2]   Deployment of hello-11_0 complete
[Worker_2]   Deploying hello-6_0
[Worker_2]     Executing create on hello-6_0
[Worker_2]     Executing start on hello-6_0
[Worker_2]   Deployment of hello-6_0 complete
[Worker_4]   Deploying hello-7_0
[Worker_4]     Executing create on hello-7_0
[Worker_4]     Executing start on hello-7_0
[Worker_4]   Deployment of hello-7_0 complete
```

