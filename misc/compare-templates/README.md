# Comparing templates
Example with opera diff and update. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example shows the possibility to update redeploy the TOSCA service template based on the differences with the one
that's already deployed. This can be achieved by using `opera update` CLI command that calculates the differences and
redeploys the solution. TO just explore the differences between TOSCA templates and instances `opera diff` CLI command
can be used.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/compare-templates
(venv) misc/compare-templates$ opera deploy -i inputs1.yaml service1.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying hello-1_0
[Worker_0]     Executing create on hello-1_0
[Worker_0]   Deployment of hello-1_0 complete
[Worker_0]   Deploying hello-2_0
[Worker_0]     Executing create on hello-2_0
[Worker_0]   Deployment of hello-2_0 complete
[Worker_0]   Deploying hello-3_0
[Worker_0]     Executing create on hello-3_0
[Worker_0]   Deployment of hello-3_0 complete
[Worker_0]   Deploying hello-4_0
[Worker_0]     Executing create on hello-4_0
[Worker_0]   Deployment of hello-4_0 complete
[Worker_0]   Deploying hello-6_0
[Worker_0]     Executing create on hello-6_0
[Worker_0]   Deployment of hello-6_0 complete

(venv) misc/compare-templates$ opera diff -i inputs2.yaml service2.yaml
nodes:
  added:
  - hello-5
  changed:
    hello-1:
      capabilities:
        deleted:
        - test
      interfaces:
        Standard:
          operations:
            create:
              artifacts:
                added:
                - lib/files/file1_2.yaml
                deleted:
                - lib/files/file1_1.yaml
              inputs:
                marker:
                - marker1
                - marker2
                time:
                - '0'
                - '1'
            delete:
              artifacts:
                added:
                - lib/files/file1_2.yaml
                deleted:
                - lib/files/file1_1.yaml
              inputs:
                marker:
                - marker1
                - marker2
                time:
                - '0'
                - '1'
      properties:
        time:
        - '0'
        - '1'
    hello-2:
      capabilities:
        test:
          properties:
            test1:
            - '2'
            - '3'
            test2:
            - '2'
            - '3'
      dependencies:
      - hello-2
      interfaces:
        Standard:
          operations:
            create:
              artifacts:
                added:
                - lib/files/file2.yaml
                deleted:
                - lib/files/file1_1.yaml
              inputs:
                marker:
                - marker1
                - marker2
            delete:
              artifacts:
                added:
                - lib/files/file2.yaml
                deleted:
                - lib/files/file1_1.yaml
              inputs:
                marker:
                - marker1
                - marker2
      properties:
        day:
        - '1'
        - '2'
      requirements:
        added:
        - dependency
      types:
      - hello_type_old
      - hello_type_new
    hello-3:
      interfaces:
        Standard:
          operations:
            create:
              inputs:
                marker:
                - marker1
                - marker2
            delete:
              inputs:
                marker:
                - marker1
                - marker2
    hello-6:
      dependencies:
      - hello-6
      interfaces:
        Standard:
          operations:
            create:
              inputs:
                marker:
                - marker1
                - marker2
            delete:
              inputs:
                marker:
                - marker1
                - marker2
      requirements:
        dependency:
          target:
          - hello-1
          - hello-2
  deleted:
  - hello-4

(venv) misc/compare-templates$ opera update -i inputs2.yaml service2.yaml
[Worker_0]   Undeploying hello-2_0
[Worker_0]     Executing delete on hello-2_0
[Worker_0]   Undeployment of hello-2_0 complete
[Worker_0]   Undeploying hello-3_0
[Worker_0]     Executing delete on hello-3_0
[Worker_0]   Undeployment of hello-3_0 complete
[Worker_0]   Undeploying hello-4_0
[Worker_0]     Executing delete on hello-4_0
[Worker_0]   Undeployment of hello-4_0 complete
[Worker_0]   Undeploying hello-6_0
[Worker_0]     Executing delete on hello-6_0
[Worker_0]   Undeployment of hello-6_0 complete
[Worker_0]   Undeploying hello-1_0
[Worker_0]     Executing delete on hello-1_0
[Worker_0]   Undeployment of hello-1_0 complete
[Worker_0]   Deploying hello-1_0
[Worker_0]     Executing create on hello-1_0
[Worker_0]   Deployment of hello-1_0 complete
[Worker_0]   Deploying hello-2_0
[Worker_0]     Executing create on hello-2_0
[Worker_0]   Deployment of hello-2_0 complete
[Worker_0]   Deploying hello-3_0
[Worker_0]     Executing create on hello-3_0
[Worker_0]   Deployment of hello-3_0 complete
[Worker_0]   Deploying hello-5_0
[Worker_0]     Executing create on hello-5_0
[Worker_0]   Deployment of hello-5_0 complete
[Worker_0]   Deploying hello-6_0
[Worker_0]     Executing create on hello-6_0
[Worker_0]   Deployment of hello-6_0 complete
```

