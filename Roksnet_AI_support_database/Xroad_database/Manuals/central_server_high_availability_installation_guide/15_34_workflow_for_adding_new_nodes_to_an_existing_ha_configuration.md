### 3.4 Workflow for Adding New Nodes to an Existing HA Configuration

Referencing steps in section [4](#4-general-installation-of-ha-support).

1.  Upgrade the software of the existing nodes to the latest version available, verify system health on all nodes.
2.  Create a backup system configuration of the existing nodes and store it in a safe place.
3.  Prepare the node for HA configuration as described in section [4](#4-general-installation-of-ha-support).
4.  Install the X-Road Central Server software as described in the X-Road Central Server Installation Guide \[[IG-CS](#Ref_IG-CS)\] to each of the new nodes.

After installing and configuring all the X-Road Central Server nodes, retrieve new internal end external configuration anchor files from one of the nodes and distribute the files to all Security Servers and configuration proxies.