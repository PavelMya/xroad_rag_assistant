### C.3 Remote Database

It is possible to use a remote database with Central Server. This option is sometimes used in development when there's need to externalize the database state.

Central Server supports a variety of cloud databases including AWS RDS and Azure Database for PostgreSQL. This deployment option is useful when doing development in cloud environment.

![Central Server with remote database](img/ig-cs_remote_db.svg)

Central Server itself can also be clustered. In clustered mode high-availability is built in to the system and the clients (Security Servers and configuration proxies) can continue operation despite a loss of a Central Server node.

![Central Server cluster with remote database](img/ig-cs_cluster_remote_db.svg)