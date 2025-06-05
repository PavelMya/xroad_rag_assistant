# wal_keep_size = 8        # on PostgreSQL >= 13

hot_standby = on
hot_standby_feedback = on
```

*On Ubuntu, RHEL (PostgreSQL >=12) only*, add the primary_conninfo to postgresql.conf:
```properties
primary_conninfo = 'host=<primary> port=5433 user=<nodename> sslmode=verify-ca sslcert=/etc/xroad/postgresql/server.crt sslkey=/etc/xroad/postgresql/server.key sslrootcert=/etc/xroad/postgresql/ca.crt'
```
Where, as above, `<primary>` is the DNS or IP address of the primary node and `<nodename>` is the node name (the replication user name added to the primary database).

Notice that on RHEL, during `pg_basebackup` the `postgresql.conf` was copied from the primary node so the WAL sender
parameters should be disabled. Also check that `listen_addresses` is localhost-only.

Finally, start the database instance

**RHEL:**
```bash
systemctl start postgresql-serverconf
```

**Ubuntu:**
```bash
systemctl start postgresql@<postgresql major version>-serverconf
```