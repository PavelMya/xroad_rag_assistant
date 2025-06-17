### 6.3 Verifying replication from the admin user interface

Verifying the cluster setup via the admin interface requires the cluster to be part of an existing X-Road instance like
`FI-DEV` or `FI-TEST` or using a custom, configured X-Road environment with at least a Central Server and the security
server cluster behind a load balancer.

To test the configuration file replication from the admin user interface, a key can be created in the admin interface of the
primary node. In addition, a certificate signing request can be created for the key in the UI, downloaded, signed by an
external CA and then uploaded back to the admin UI. For help on these tasks, see the  Security Server User Guide
\[[UG-SS](#13-references)\].

The keys and certificate changes should be propagated to the secondary nodes in a few minutes.

The `serverconf` database replication can also be tested on the admin UI once the basic configuration, as mentioned in
[3. X-Road Installation and configuration](#3-x-road-installation-and-configuration) is done. A new subsystem can be added
to the primary node. A registration request can be sent to the Central Server, but it is not required. The added subsystem
should appear on the secondary nodes immediately.

## 7. Upgrading a clustered X-Road Security Server installation

This chapter briefly discusses ways of upgrading the X-Road software in a clustered environment. The offline option will
disrupt message delivery while the online option should allow upgrades with minimal disruption.