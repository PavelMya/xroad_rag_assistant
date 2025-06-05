#### Automatic fail-over

Achieving and maintaining a system with automated fail-over is a complex task and out of the scope of this guide. Some actively maintained open-source solutions for automating PostgreSQL failover include:

* Microsoft (Citus Data) pg_auto_failover: https://pg-auto-failover.readthedocs.io/en/latest/index.html
  * A straightforward solution for a two-node (primary-standby) setup. In addition to the data nodes, it requires a monitoring server (also a PostgreSQL instance).
* 2ndQuadrant Repmgr: https://repmgr.org/
  * An established solution for managing PostgreSQL replication and fail-over. Can handle more complex setups (e.g. several replicas) than pg_auto_failover.
* Patroni by Zalando: https://patroni.readthedocs.io/en/latest/
  * "Patroni is a template for you to create your own customized, high-availability solution using Python and a distributed configuration store like ZooKeeper, etcd, Consul or Kubernetes"
* ClusterLabs PostgreSQL Automatic Failover (PAF): http://clusterlabs.github.io/PAF/documentation.html
  * PAF is a resource agent for Pacemaker cluster resource manager; probably the most versatile but also most difficult to configure and operate.