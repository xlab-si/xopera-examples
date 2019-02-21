Introduction
============

This repository contains working examples of blueprints for the
`xOpera orchestrator`_ ``opera``. Their aim is to help authors of `OASIS TOSCA`_
service templates get started with OASIS YAML Simple Profile v1.2 and the
use of `Ansible automation`_ for implementing TOSCA interfaces.

The only requirement for the examples to work is that we have the ``opera``
installed as detailed in the tool's Prerequisites and Installation section
of the `opera README.rst`_. Each example is located in its own self-contained
directory.

.. _xOpera orchestrator: https://github.com/xlab-si/xopera-opera
.. _OASIS TOSCA: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca
.. _Ansible automation: https://www.ansible.com/
.. _opera README.rst: https://github.com/xlab-si/xopera-opera/blob/master/README.rst


01 Hello world
==============

The first example is in ``01-hello-world/``. The ``service.yaml`` within this
directory shows a minimal service template that is composed of two node
templates:

* ``hello``: a node template of type ``tosca.nodes.SoftwareComponent`` that
  invokes the ``playbooks/hello/create.yml`` Ansible playbook as its
  ``create`` interface.
* ``my-workstation``: this node template is necessary to fulfil the
  ``hello``'s requirement for capability ``host``. By assigning ``localhost``
  as the values of the node template's attributes ``private_address`` and
  ``public_address`` we tell the ``opera`` orchestrator that it should
  host ``hello`` on the same workstation as we are running the ``opera``
  from.

We can run our hello-world as follows::

     (venv) $ cd 01-hello-world
     (venv) 01-hello-world$ opera deploy hello-world service.yaml
     Loading service template ...
     Resolving service template links ...
     Creating instance model ...
     Deploying instance model ...
       Processing my-workstation.0 ...
       Processing hello.0 ...
         Executing primary: playbooks/hello/create.yml ...
     Done.

The result of this service template should be a new directory and a file on
the workstation::

     (venv) 01-hello-world$ ls -lh /tmp/playing-opera/hello/
     total 0
     -rw-rw-rw- 1 matej matej 0 Feb 20 16:02 hello.txt


02 Server - Client
==================

The second example aims at showing how we can establish a sense of dependency
between two node templates. It also shows one way of using a run-time attribute
from a "server" node template in the "client" node template, thus establishing
a dependency binding.

If we open the service template ``02-server-client/service.yaml``, we will find
a simple topology template composed of three node templates:

* ``my-workstation``: like before, this node template provides the ``host``
  capability required by the other node templates, telling the orchestrator
  to execute the operations on our local workstation.
* ``my-mock-server``: a mock component designated to have serving
  capabilities.
* ``my-mock-client``: a mock component acting as a client to the
  ``my-mock-server``.

A good TOSCA service template design should move as much as possible to the
type and relationship definitions, leaving the topology template as simple
and easy to read as possible. This is what we've done in the example, having
kept in mind the knowledge (discerned from peeking into those Ansible playbooks)
that:

* Both mock components, i.e., the server and the client, need the property
  ``path``, because they use this information to know where to get installed
  into.
* Both components generate a random ID.
* The binding of a client to a server takes a form of the client writing the
  server's ID into its own configuration.

All of this went into the decision to create the common node type
``my.nodes.MockComponent`` that declares the property and the attribute shared
by both the client and the server component. We then derive
``my.nodes.MockServer`` from this type, declaring the ``server`` capability and
defining the interface specific to the server component. Note that we allowed
the source node templates, i.e., the ones that need to connect to a server, to
be any component. We will tighten this down later.

The interesting part is when we derive ``my.nodes.MockComponent`` into the
``my.nodes.MockClient``. Here, we make explicit that the node templates of
this type require a ``server``, and with the relationship type
``my.relationships.MockServerClient`` we also make sure that only node templates
of type ``my.nodes.MockServer`` will be connected.

The final bit of work is the definition of all the interfaces. We wire the
interface operations to their respective Ansible playbooks. There are just
two simple rules:

* Any inputs declared for the operation in the TOSCA service templates will
  appear as variables in the Ansible play.
* The Ansible playbook invokes module ``set_stats`` in a task to set the
  values of the node template instance's attributes as side-effects of the
  operation's run.

The client configuration operation needs the server's ID to be known, therefore
we declare the ``server_id`` input to the ``configure`` interface. Thanks to the
way we defined the types and the relationships, we can expect that in a topology
template, it will be possible to resolve a requirement named ``server`` that
will have an already known value of attribute ``id`` representing exactly the
information that the client needs. Hence, using
``get_attribute: [ SELF, server, id]`` works.

Having gone through all that, let's now finally run the service template::

       (venv) $ cd 02-server-client
       (venv) 02-server-client$ opera deploy server-client service.yaml
       Loading service template ...
       Resolving service template links ...
       Creating instance model ...
       Deploying instance model ...
         Processing my-workstation.0 ...
         Processing my-mock-server.0 ...
           Executing primary: playbooks/mock-server/create.yml ...
         Processing my-mock-client.0 ...
           Executing primary: playbooks/mock-client/create.yml ...
           Executing primary: playbooks/mock-client/configure.yml ...
       Done.

The output shows that the order in which the node templates are instantiated
and their respective operations executed is as expected. The orchestrator
starts with ``my-workstation``, because it depends on nothing else. The
``my-mock-server`` is next, because it depends only on ``my-workstation``.
Finally, the orchestrator creates and configures ``my-mock-client``.

We can also make sure that the playbooks created the configurations as
promised::

       (venv) $ cat /tmp/playing-opera/02/server/server.conf
       SERVER_ID=470003
     
       (venv) $ cat /tmp/playing-opera/02/client/client.conf
       CLIENT_ID=427045
       SERVER_ID=470003


License
=======

.. image:: http://i.creativecommons.org/l/by/3.0/88x31.png
   :alt: Creative Commons License

This work is licensed under a `Creative Commons Attribution 3.0 Unported License`_

.. _Creative Commons Attribution 3.0 Unported License: http://creativecommons.org/licenses/by/3.0/deed.en_US