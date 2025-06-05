### 3.5 Post-Configuration Steps

If the remote database supports fail over to a secondary host (e.g. when using PostgreSQL streaming replication with hot-standby), it is possible to define the secondary database hosts in `/etc/xroad/db.properties`. The system will automatically try the secondary hosts in case the primary fails.

```properties
secondary_hosts=<comma separated list of hosts>