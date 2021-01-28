# Server - Client
Establish a connection between two TOSCA node templates.

## Table of Contents
  - [Description](#description)
  - [Running with xOpera](#running-with-xopera)

# Description
The second example aims at showing how we can establish a sense of dependency
between two node templates. It also shows one way of using a run-time attribute
from a "server" node template in the "client" node template, thus establishing
a dependency binding.

If we open the service template `02-server-client/service.yaml`, we will find
a simple topology template composed of three node templates:

- `my-workstation`: like before, this node template provides the `host`
  capability required by the other node templates, telling the orchestrator
  to execute the operations on our local workstation.
- `my-mock-server`: a mock component designated to have serving
  capabilities.
- `my-mock-client`: a mock component acting as a client to the
  `my-mock-server`.

A good TOSCA service template design should move as much as possible to the
type and relationship definitions, leaving the topology template as simple
and easy to read as possible. This is what we've done in the example, having
kept in mind the knowledge (discerned from peeking into those Ansible playbooks)
that:

- Both mock components, i.e., the server and the client, need the property
  `path`, because they use this information to know where to get installed
  into.
- Both components generate a random ID.
- The binding of a client to a server takes a form of the client writing the
  server's ID into its own configuration.

All of this went into the decision to create the common node type
`my.nodes.MockComponent` that declares the property and the attribute shared
by both the client and the server component. We then derive
`my.nodes.MockServer` from this type, declaring the `server` capability and
defining the interface specific to the server component. Note that we allowed
the source node templates, i.e., the ones that need to connect to a server, to
be any component. We will tighten this down later.

The interesting part is when we derive `my.nodes.MockComponent` into the
`my.nodes.MockClient`. Here, we make explicit that the node templates of
this type require a `server`, and with the relationship type
`my.relationships.MockServerClient` we also make sure that only node templates
of type `my.nodes.MockServer` will be connected.

The final bit of work is the definition of all the interfaces. We wire the
interface operations to their respective Ansible playbooks. There are just
two simple rules:

* Any inputs declared for the operation in the TOSCA service templates will
  appear as variables in the Ansible play.
* The Ansible playbook invokes module `set_stats` in a task to set the
  values of the node template instance's attributes as side-effects of the
  operation's run.

The client configuration operation needs the server's ID to be known, therefore
we declare the `server_id` input to the `configure` interface. Thanks to the
way we defined the types and the relationships, we can expect that in a topology
template, it will be possible to resolve a requirement named `server` that
will have an already known value of attribute `id` representing exactly the
information that the client needs. Hence, using
`get_attribute: [ SELF, server, id]` works.

# Running with xOpera
Having gone through all that, let's now finally run the service template:

```console
(venv) $ cd misc/server-client
(venv) misc/server-client$ opera deploy service.yaml
[Worker_0]   Deploying my-workstation_0
[Worker_0]   Deployment of my-workstation_0 complete
[Worker_0]   Deploying my-mock-server_0
[Worker_0]     Executing create on my-mock-server_0
[Worker_0]   Deployment of my-mock-server_0 complete
[Worker_0]   Deploying my-mock-client_0
[Worker_0]     Executing create on my-mock-client_0
[Worker_0]     Executing configure on my-mock-client_0
[Worker_0]   Deployment of my-mock-client_0 complete
```

The output shows that the order in which the node templates are instantiated
and their respective operations executed is as expected. The orchestrator
starts with `my-workstation`, because it depends on nothing else. The
`my-mock-server` is next, because it depends only on `my-workstation`.
Finally, the orchestrator creates and configures `my-mock-client`.

We can also make sure that the playbooks created the configurations as
promised:

```console
(venv) $ cat /tmp/playing-opera/02/server/server.conf
SERVER_ID=470003

(venv) $ cat /tmp/playing-opera/02/client/client.conf
CLIENT_ID=427045
SERVER_ID=470003
```
