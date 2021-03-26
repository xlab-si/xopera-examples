# Scaling
An example of AWS Lambda scaling with TOSCA policies.

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
This example displays the possible scaling TOSCA template for AWS Lambda with two nodes - one for AWS Lambda and the 
second for monitoring configuration. There are also two policies for scaling up and down, which include two triggers 
that are invoked after the validation and deployment with opera notify. In the end the example can also be undeployed. 
The playbooks include just some debug messages with some variables (inputs) from policies or with the `notification` 
variable that holds the contents from the notification file.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd misc/scaling
(venv) misc/scaling$ opera deploy service.yaml
[Worker_0]   Deploying aws_lambda_0
[Worker_0]     Executing create on aws_lambda_0
[Worker_0]   Deployment of aws_lambda_0 complete
[Worker_0]   Deploying configure_monitoring_0
[Worker_0]     Executing configure on configure_monitoring_0
[Worker_0]   Deployment of configure_monitoring_0 complete

# scale down by calling scale_down_trigger event with notification_scale_down.json notification file
(venv) misc/scaling$ opera notify -e scale_down_trigger -n files/notification_scale_down.json
[Worker_0]   Notifying aws_lambda_0
[Worker_0]    Calling trigger radon.triggers.scaling.ScaleDown with event scale_down_trigger
[Worker_0]     Executing scale_down on aws_lambda_0
[Worker_0]    Calling trigger actions with event scale_down_trigger complete
[Worker_0]   Notification on aws_lambda_0 complete
[Worker_0]   Notifying configure_monitoring_0
[Worker_0]   Notification on configure_monitoring_0 complete

# scale up by calling scale_up_trigger event with notification_scale_up.json notification file
(venv) misc/scaling$ opera notify -e scale_up_trigger -n files/notification_scale_up.json
[Worker_0]   Notifying aws_lambda_0
[Worker_0]    Calling trigger radon.triggers.scaling.ScaleUp with event scale_up_trigger
[Worker_0]     Executing scale_up on aws_lambda_0
[Worker_0]    Calling trigger actions with event scale_up_trigger complete
[Worker_0]   Notification on aws_lambda_0 complete
[Worker_0]   Notifying configure_monitoring_0
[Worker_0]   Notification on configure_monitoring_0 complete

(venv) misc/scaling$ opera undeploy
[Worker_0]   Undeploying aws_lambda_0
[Worker_0]     Executing delete on aws_lambda_0
[Worker_0]   Undeployment of aws_lambda_0 complete
[Worker_0]   Undeploying configure_monitoring_0
[Worker_0]   Undeployment of configure_monitoring_0 complete
```
