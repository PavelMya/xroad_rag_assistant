### 4.3 Configuring the primary instance for replication

Edit `postgresql.conf` and set the following options:
>* On RHEL, we assume that default configuration files are located in the `PGDATA` directory `/var/lib/pgsql/serverconf`.
>  * **Note:** depending on the PostgreSQL installation, the configuration files can be located in different directory, for example `/var/lib/pgsql/13/serverconf`.
>* Ubuntu keeps the config in `/etc/postgresql/<postgresql major version>/<cluster name>`, e.g. `/etc/postgresql/10/serverconf`.

```properties
ssl = on
ssl_ca_file   = '/etc/xroad/postgresql/ca.crt'
ssl_cert_file = '/etc/xroad/postgresql/server.crt'
ssl_key_file  = '/etc/xroad/postgresql/server.key'

listen_addresses  = '*'  # (default is localhost. Alternatively: localhost, <IP of the interface the secondaries connect to>")