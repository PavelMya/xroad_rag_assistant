#### 4.3.1 Notes on HA Setup

In an HA setup, the address of the Central Server is local to the node that is being configured.

In an HA setup, internal and external configuration anchors contain information about each Central Server that is part of the cluster. If the address of one of the servers is changed, configuration anchors will be re-generated automatically on all the nodes.