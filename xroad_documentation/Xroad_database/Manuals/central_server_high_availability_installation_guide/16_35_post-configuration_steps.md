### 3.5 Post-Configuration Steps

If the remote database supports fail over to a secondary host (e.g. when using PostgreSQL streaming replication with hot-standby), it is possible to define the secondary database hosts in `/etc/xroad/db.properties`. The system will automatically try the secondary hosts in case the primary fails.

```properties
secondary_hosts=

# Example:

# secondary_hosts=standby.example.org,standby2.example.org
```

The secondary hosts are assumed to use the same port (default 5432) as the primary host.