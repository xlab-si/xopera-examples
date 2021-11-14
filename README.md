# xOpera examples
Deployable TOSCA YAML v1.3 templates for [xOpera orchestration tool](https://github.com/xlab-si/xopera-opera).

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/xlab-si/xopera-examples/Validate%20examples%20with%20xOpera%20orchestrator?label=validation)](https://github.com/xlab-si/xopera-examples/actions?query=workflow%3A%22Validate+examples+with+xOpera+orchestrator%22)
[![GitHub contributors](https://img.shields.io/github/contributors/xlab-si/xopera-examples)](https://github.com/xlab-si/xopera-examples/graphs/contributors)

## Table of Contents
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgement](#acknowledgement)

## Introduction
This repository contains working examples of blueprints (TOSCA templates and their implementations) for the
[xOpera orchestrator](https://github.com/xlab-si/xopera-opera) `opera`. Their aim is to help authors of 
[OASIS TOSCA](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca) service templates get started with 
[OASIS YAML Simple Profile v1.3](https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/cos01/TOSCA-Simple-Profile-YAML-v1.3-cos01.html) 
and the use of [Ansible automation](https://www.ansible.com/) for implementing TOSCA interfaces.
The examples here are also explained more in detail within the [xOpera documentation](https://xlab-si.github.io/xopera-docs/examples.html) page.

## Prerequisites
The main requirement for the examples to work is that we have the ``opera`` installed as detailed in the tool's 
Prerequisites and Installation section of the [opera README.md](https://github.com/xlab-si/xopera-opera/blob/master/README.md). 
Each example is located in its own self-contained directory and contains README with some basic info about its purpose 
and running. Some examples may require special  resources, like infrastructure (OpenStack), cloud provider accounts 
(AWS, Azure, GCP).

## License
![Creative Commons License](https://licensebuttons.net/l/by/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

## Contact
You can contact the xOpera team by sending an email to [xopera@xlab.si](mailto:xopera@xlab.si).

## Acknowledgement
Some work from this project has received funding from the European Union’s Horizon 2020
research and innovation programme under Grant Agreements No. 825040 
([RADON](http://radon-h2020.eu/)), No. 825480 ([SODALITE](http://www.sodalite.eu/)) and No. 101000162 ([PIACERE](https://www.piacere-project.eu/)).
