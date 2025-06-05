# PostgreSQL >=13 (RHEL 9, Ubuntu 22.04, 24.04)
wal_level = replica

max_wal_senders = 3   # should be ~ number of secondaries plus some small number. Here, we assume there are two secondaries.
wal_keep_size   = 8   # keep some wal size so that secondaries that are offline can catch up.
```

For more information about the streaming replication configuration options,
see the [PostgreSQL documentation](https://www.postgresql.org/docs/10/runtime-config-replication.html).

Edit `pg_hba.conf` and enable connections to the replication pseudo database using client certificates. See chapter
[4.1](#41-setting-up-tls-certificates-for-database-authentication) for the authentication setup.

```
hostssl     replication     +slavenode  samenet     cert
```
**Note:** The CN field in the certificate subject must match a replication user name in postgresql. 
See the [PostgreSQL documentation](https://www.postgresql.org/docs/10/auth-pg-hba-conf.html) for more details.

The `samenet` above assumes that the secondaries will be in the same subnet as the primary.

Start the primary instance:

**Ubuntu:**

```bash
systemctl start postgresql@<postgresql major version>-serverconf
```

**RHEL:**

```bash
systemctl start postgresql-serverconf
```

Create the replication user(s) with password authentication disabled:
```bash
sudo -u postgres psql -p 5433 -c "CREATE ROLE slavenode NOLOGIN";
sudo -u postgres psql -p 5433 -c "CREATE USER "<nodename>" REPLICATION PASSWORD NULL IN ROLE slavenode";
```

Create a user named `serverconf` for local `serverconf` database access:

```bash
sudo -u postgres psql -p 5433 -c "CREATE USER serverconf PASSWORD '<password>'";
```

Copy the `serverconf` database from the default instance to the new instance:

```bash
sudo -u postgres pg_dump -C serverconf | sudo -u postgres psql -p 5433 -f -
```

To avoid confusion, the *old* `serverconf` database on the primary should be renamed, or even deleted.
```bash
sudo -u postgres psql -p 5432 -c "ALTER DATABASE serverconf RENAME TO serverconf_old";
```