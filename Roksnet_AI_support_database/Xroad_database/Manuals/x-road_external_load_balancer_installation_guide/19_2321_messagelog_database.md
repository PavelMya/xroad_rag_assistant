##### 2.3.2.1 `messagelog` database

The messagelog database is not replicated. Each node has its own separate messagelog database. **However**, in order to
support PostgreSQL streaming replication (hot standby mode) for the serverconf data, the serverconf and messagelog
databases must be separated. This requires modifications to the installation (a separate PostgreSQL instance is needed
for the messagelog database) and has some implications on the Security Server resource requirements as a separate
instance uses some memory.

##### 2.3.2.2 OCSP responses from `/var/cache/xroad/`

The OCSP responses are currently not replicated. Replicating them could make the cluster more fault tolerant but the
replication cannot simultaneously create a single point of failure. A distributed cache could be used for the responses.

## 3. X-Road Installation and configuration

This chapter details the complete installation on a high level, with links to other chapters that go into the details.

You can set up the cluster manually, or use the provided Ansible playbook \[[SS-CLUSTER](#13-references)\] if it suits
your purposes.

### 3.1 Prerequisites

In order to properly set up the data replication, the secondary nodes must be able to connect to:
* the primary server using SSH (tcp port 22), and
* the primary `serverconf` database (e.g. tcp port 5433).