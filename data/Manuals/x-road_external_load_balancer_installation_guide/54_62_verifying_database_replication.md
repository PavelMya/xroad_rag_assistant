### 6.2 Verifying database replication

To see if the database replication is working, connect to the new `serverconf` instance on the primary node and verify
that the secondary nodes are listed.
```bash
sudo -u postgres psql -p 5433 -c "select * from pg_stat_replication;"
```
A successful replication with two secondary nodes could look like this:

| pid  | usesysid | usename  | application_name | client_addr    | client_hostname | client_port | backend_start                 | state     | sent_location | write_location | flush_location | replay_location | sync_priority | sync_state |
| ---- | -------- | -------- | ---------------- | -------------- | --------------- | ----------- | ----------------------------- | --------- | ------------- | -------------- | -------------- | --------------- | ------------- | ---------- |
| 1890 | 16719    | hdev-ss3 | walreceiver      | 172.31.128.151 |                 | 45275       | 2017-03-10 06:30:50.470084+02 | streaming | 0/4058A40     | 0/4058A40      | 0/4058A40      | 0/4058A40       | 0             | async      |
| 1891 | 16718    | hdev-ss2 | walreceiver      | 172.31.128.82  |                 | 50174       | 2017-03-10 06:30:50.918481+02 | streaming | 0/4058A40     | 0/4058A40      | 0/4058A40      | 0/4058A40       | 0             | async      |

For more information on the `pg_stat_replication` view, see the [PostgreSQL documentation](https://www.postgresql.org/docs/10/monitoring-stats.html#PG-STAT-REPLICATION-VIEW).