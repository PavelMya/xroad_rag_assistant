### Migrating from Standalone to HA Cluster

Since version 6.23.0 it is possible to use an external database for the Central Server. This is the basis of the currently recommended Central Server HA solution. It is possible to migrate a standalone Central Server (version 6.23.0 or later) to the cluster based HA solution with the following steps.

1. Take a backup of the Central Server.

2. Follow the instructions in [Central Server User Guide](ug-cs_x-road_6_central_server_user_guide.md#17-migrating-to-remote-database-host) to migrate the Central Server database from local to remote.

3. Follow the instructions in [General Installation of HA Support](#4-general-installation-of-ha-support)

4. Setup the database cluster as instructed in [Appendix A. Setting up a replicated PostgreSQL database](#appendix-a-setting-up-a-replicated-postgresql-database).