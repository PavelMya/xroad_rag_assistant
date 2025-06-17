### 4.3 Configuring the primary instance for replication

Edit `postgresql.conf` and set the following options:
>* On RHEL, we assume that default configuration files are located in the `PGDATA` directory `/var/lib/pgsql/serverconf`.
>  * **Note:** depending on the PostgreSQL installation, the configuration files can be located in different directory, for example `/var/lib/pgsql/13/serverconf`.
>* Ubuntu keeps the config in `/etc/postgresql//`, e.g. `/etc/postgresql/10/serverconf`.

```properties
ssl = on
ssl_ca_file   = '/etc/xroad/postgresql/ca.crt'
ssl_cert_file = '/etc/xroad/postgresql/server.crt'
ssl_key_file  = '/etc/xroad/postgresql/server.key'

listen_addresses  = '*'  # (default is localhost. Alternatively: localhost, ")

# PostgreSQL 9.2 (RHEL 7)
wal_level = hot_standby

# PostgreSQL 10 & 12 (RHEL 7, 8; Ubuntu 20.04)
wal_level = replica

max_wal_senders   = 3   # should be ~ number of secondaries plus some small number. Here, we assume there are two secondaries.
wal_keep_segments = 8   # keep some wal segments so that secondaries that are offline can catch up.