# Enables read-only queries on the standby, ignored by master
hot_standby = on
```

Edit pg_hba.conf (on Ubuntu by default in `/etc/postgresql/<version>/<cluster name>/`) and add configuration for the replication user. For example, the following allows the user "standby" from a host in the same network to connect to the master. The connection requires TLS and uses challenge-response password authentication. See https://www.postgresql.org/docs/current/auth-pg-hba-conf.html for more information.

```