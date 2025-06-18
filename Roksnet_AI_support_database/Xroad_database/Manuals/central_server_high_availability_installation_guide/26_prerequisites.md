### Prerequisites

* Same version (10 or later) of PostgreSQL installed on at least two similar hosts.
* Network connections on PostgreSQL port (tcp/5432) are allowed between database servers (both directions).
* Network connections to PostgreSQL port (tcp/5432) are allowed from the Central Servers to the database servers.

### PostgreSQL configuration (all database servers)

Edit `postgresql.conf` and verify the following settings:
* Ubuntu: `/etc/postgresql///postgresql.conf`
* RHEL: In data directory, usually `/var/lib/pgsql/data`

```properties

# more secure password encryption (optional but recommended)
password_encryption = scram-sha-256

# ssl should be enabled (optional but recommended)
ssl on

# network interfaces to listen on (default is localhost)
listen_addresses = '*'

# WAL replication settings

# write ahead log level
wal_level = replica

# Enable replication connections

# See: https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS
max_wal_senders = 10

# See: https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS
max_replication_slots = 10