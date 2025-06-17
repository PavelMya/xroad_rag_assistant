## 3. Standalone and High-Availability Systems

The Central Server can be installed and configured in several ways:
- A standalone server with local database
- A standalone server with remote database
- A cluster of Central Servers (nodes) using a remote database. The system continues to function if one or more of the Central Server nodes are experiencing problems or are down for maintenance. If the database is highly available (e.g using hot-standby with automatic fail-over or multi-master replication), the system can also recover from database problems with minimal downtime.

When the system is configured with the most basic option standalone server with local database, there is no high-availability support. If either the web server or the database server break, the system goes down.

In the case of an HA setup, the Central Servers share configuration via an optionally highly-available database. While most of the system settings described in this document apply to the whole cluster, some have a meaning that is local to each node. In addition, all the configuration signing keys are local to each node and must be generated separately. This distinction will be stated explicitly throughout this document, where necessary.

In an HA setup, if the system is configured using different nodes in parallel, the effect will be similar to several people updating the configuration of a standalone server at the same time.