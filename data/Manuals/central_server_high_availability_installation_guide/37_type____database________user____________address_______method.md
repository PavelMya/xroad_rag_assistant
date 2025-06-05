# TYPE    DATABASE        USER            ADDRESS       METHOD
hostssl   replication     standby         samenet       scram-sha-256
```

Restart the master PostgreSQL instance before continuing.

On the master server, create the replication user:
```bash
sudo -iu postgres psql -c "CREATE USER standby REPLICATION PASSWORD '<password>'"
```

Also on master, create a replication slot for the standby. Replication slots provide an automated way to ensure that the master does not remove write-ahead-log segments until they have been received by a standby, even when standby is disconnected (see https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS).

```bash
sudo -iu postgres psql -c "SELECT pg_create_physical_replication_slot('standby_node1');"
```