# xOpera examples
Deployable TOSCA YAML v1.3 templates for [xOpera TOSCA orchestration tool].

[![validate](https://github.com/xlab-si/xopera-examples/actions/workflows/validate.yaml/badge.svg)](https://github.com/xlab-si/xopera-examples/actions/workflows/validate.yaml)
[![GitHub contributors](https://img.shields.io/github/contributors/xlab-si/xopera-examples)](https://github.com/xlab-si/xopera-examples/graphs/contributors)

## Table of Contents
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgement](#acknowledgement)

## Introduction
This repository contains working examples of blueprints (TOSCA templates and their implementations) for the
[xOpera orchestrator] `opera`. 
Their aim is to help authors and developers of [OASIS TOSCA] service templates get started with 
[OASIS YAML Simple Profile v1.3] and the use of [Ansible] automation tool for implementing TOSCA interface operations.
The examples here are also explained more in detail within the [xOpera documentation] page.

## Prerequisites
The main requirement for the examples to work is that we have the ``opera`` installed as detailed in the tool's 
*Prerequisites and Installation* section of the [opera README.md]. 
Each example is located in its own self-contained directory and contains README with some basic info about its purpose 
and running. 
Some examples may require special  resources, like infrastructure (OpenStack), cloud provider accounts (AWS, Azure, 
GCP).

## License
![Creative Commons License](https://licensebuttons.net/l/by/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution 4.0 International].

## Contact
You can contact the xOpera team by sending an email to [xopera@xlab.si].

## Acknowledgement
Some work from this project has received funding from the European Union’s Horizon 2020 research and innovation 
programme under Grant Agreements No. 825040 ([RADON]), No. 825480 ([SODALITE]) and No. 101000162 ([PIACERE]).

[xOpera TOSCA orchestration tool]: https://github.com/xlab-si/xopera-opera
[xOpera orchestrator]: https://github.com/xlab-si/xopera-opera
[OASIS TOSCA]: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca
[OASIS YAML Simple Profile v1.3]: https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/cos01/TOSCA-Simple-Profile-YAML-v1.3-cos01.html
[Ansible]: https://www.ansible.com/
[xOpera documentation]: https://xlab-si.github.io/xopera-docs/examples.html
[opera README.md]: https://github.com/xlab-si/xopera-opera/blob/master/README.md
[Creative Commons Attribution 4.0 International]: https://creativecommons.org/licenses/by/4.0/
[xopera@xlab.si]: mailto:xopera@xlab.si
[RADON]: http://radon-h2020.eu
[SODALITE]: http://www.sodalite.eu/
[PIACERE]: https://www.piacere-project.eu/
