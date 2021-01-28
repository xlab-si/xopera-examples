# Attribute mapping
This is an example with TOSCA attribute mapping. 

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The example shows the possible usage of TOSCA attribute mapping on teacher-student example where the list of students
attribute is populated via teacher-student relationships.

# Running with xOpera
We can run this example as follows:

```console
(venv) $ cd tosca/attribute-mapping
(venv) tosca/attribute-mapping$ opera deploy service.yaml
[Worker_0]   Deploying student-ben_0
[Worker_0]     Executing create on student-ben_0
[Worker_0]   Deployment of student-ben_0 complete
[Worker_0]   Deploying student-anne_0
[Worker_0]     Executing create on student-anne_0
[Worker_0]   Deployment of student-anne_0 complete
[Worker_0]   Deploying student-tina_0
[Worker_0]     Executing create on student-tina_0
[Worker_0]   Deployment of student-tina_0 complete
[Worker_0]   Deploying student-chris_0
[Worker_0]     Executing create on student-chris_0
[Worker_0]   Deployment of student-chris_0 complete
[Worker_0]   Deploying teacher-paul_0
[Worker_0]     Executing pre_configure_source on teacher-paul_0--student-ben_0
[Worker_0]     Executing pre_configure_source on teacher-paul_0--student-tina_0
[Worker_0]     Executing pre_configure_source on teacher-paul_0--student-chris_0
[Worker_0]     Executing pre_configure_source on teacher-paul_0--student-anne_0
[Worker_0]   Deployment of teacher-paul_0 complete

(venv) tosca/attribute-mapping$ opera outputs
student_id_list:
  description: The final list of IDs of Paul's students
  value:
  - student-1
  - student-4
  - student-6
  - student-3
```

