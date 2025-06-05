### 3.3 Workflow for Upgrading an Existing X-Road Central Server to an HA Configuration

1.  Upgrade the existing X-Road Central Server software to the latest release available, verify system health.
2.  Create a backup of the system configuration and store it in a safe place.
3.  Continue with HA support installation steps as described in section [4](#4-general-installation-of-ha-support).
4.  Install the X-Road Central Server software as described in the X-Road Central Server Installation Guide \[[IG-CS](#Ref_IG-CS)\] to each of the new nodes.
5.  After installing and configuring all the X-Road Central Server nodes, retrieve new internal and external configuration anchor files from one of the nodes and distribute the files to all Security Servers and configuration proxies.