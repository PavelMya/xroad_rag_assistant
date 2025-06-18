### 3.1 Requirements

The nodes must meet all the requirements listed in the X-Road Central Server Installation Guide (see \[[IG-CS](#Ref_IG-CS)\]). 
Additionally, creating an HA setup requires that all nodes can access the shared configuration database. A PostgreSQL (version 9.4 or newer) compatible database is required.

### 3.2 Workflow for a New X-Road Instance Setup

1.  Install HA support according to steps listed in section [4](#4-general-installation-of-ha-support).
2.  Install the X-Road Central Server software according to the X-Road Central Server Installation Guide \[[IG-CS](#Ref_IG-CS)\] on each node.