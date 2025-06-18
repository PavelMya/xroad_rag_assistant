### 4.4 Configuring the secondary instance for replication

Prerequisites:
* A separate postgresql instance has been created.
* TLS keys and certificates have been configured in `/etc/xroad/postgresql` as described in section
[4.1 Setting up TLS certificates for database authentication](#41-setting-up-tls-certificates-for-database-authentication)

Go to the postgresql data directory:
 * RHEL: `/var/lib/pgsql/serverconf`
    >**Note:** depending on the PostgreSQL installation, the configuration files can be located in different directory, for example `/var/lib/pgsql/13/serverconf`.
 * Ubuntu: `/var/lib/postgresql//serverconf`

Clear the data directory:

```bash
 rm -rf *
```

Then, do a base backup with `pg_basebackup`:
```bash
sudo -u postgres PGSSLMODE=verify-ca PGSSLROOTCERT=/etc/xroad/postgresql/ca.crt PGSSLCERT=/etc/xroad/postgresql/server.crt PGSSLKEY=/etc/xroad/postgresql/server.key pg_basebackup -h  -p 5433 -U  -D .
```
Where `` is the DNS or IP address of the primary node and `` is the node name (the replication user name added to the primary database).

**Note:** This warning by `pg_basebackup` can be ignored:
```
NOTICE: WAL archiving is not enabled; you must ensure that all required WAL segments are copied through other means to complete the backup
```

On *RHEL 7/8 (PostgreSQL  port=5433 user= sslmode=verify-ca sslcert=/etc/xroad/postgresql/server.crt sslkey=/etc/xroad/postgresql/server.key sslrootcert=/etc/xroad/postgresql/ca.crt'
trigger_file = '/var/lib/xroad/postgresql.trigger'
```
Where, as above, `` is the DNS or IP address of the primary node and `` is the node name (the replication user name added to the primary database).

On *Ubuntu, RHEL (PostgreSQL >=12)*, create an empty `standby.signal` file in the data directory. Set the owner of the file to `postgres:postgres`, mode `0600`.

Next, modify `postgresql.conf`:
>* On RHEL, we assume that default configuration files are located in the `PGDATA` directory `/var/lib/pgql/serverconf`.
>  * **Note:** depending on the PostgreSQL installation, the configuration files can be located in different directory, for example `/var/lib/pgsql/13/serverconf`.
>* Ubuntu keeps the config in `/etc/postgresql//`, e.g. `/etc/postgresql/12/serverconf`.
```properties
ssl = on
ssl_ca_file   = '/etc/xroad/postgresql/ca.crt'
ssl_cert_file = '/etc/xroad/postgresql/server.crt'
ssl_key_file  = '/etc/xroad/postgresql/server.key'

listen_addresses = localhost

# no need to send WAL logs

# wal_level = replica

# max_wal_senders = 3

# wal_keep_segments = 8    # on PostgreSQL in 10, 12