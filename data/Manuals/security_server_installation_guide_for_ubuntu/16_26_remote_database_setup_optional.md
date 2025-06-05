### 2.6 Remote Database Setup (optional)

*This is an optional step.* 

Optionally, the Security Server can use a remote database server. To avoid installing the default local PostgreSQL server during Security Server installation, first install the `xroad-database-remote` -package.
```bash
sudo apt install xroad-database-remote
```

For the application level backup and restore feature to work correctly, it is important to verify that the local PostgreSQL client has the same or later major version than the remote database server and, if necessary, install a different version of the `postgresql-client` package (see https://www.postgresql.org/download/linux/ubuntu/)
```bash
psql --version
psql (PostgreSQL) 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

psql -h <database host> -U <superuser> -tAc 'show server_version'
10.16 (Ubuntu 10.16-0ubuntu0.18.04.1)
```

The Security Server installer can create the database and users for you, but you need to create a configuration file containing the database administrator credentials. 

For advanced setup, e.g. when using separate servers for the databases, sharing a database with several Security Servers, or if storing the database administrator password on the Security Server is not an option, you can create the database users and structure manually as described in [Annex D Create Database Structure Manually](#annex-d-create-database-structure-manually) and then continue to section 2.7. Otherwise, perform the following steps:

Create the property file:
```bash
sudo touch /etc/xroad.properties
sudo chown root:root /etc/xroad.properties
sudo chmod 600 /etc/xroad.properties
```

Edit `/etc/xroad.properties`. See the example below. Replace parameter values with your own.
```properties
postgres.connection.password = <database superuser password>
postgres.connection.user = <database superuser name, postgres by default>
```
Note. If Microsoft Azure database for PostgreSQL is used, the connection user needs to be in format `username@hostname`.

Before continuing, test that the connection to the database works, e.g.
```bash
psql -h <database host> -U <superuser> -tAc 'show server_version'
```

For additional security, the `postgresql.connection.*` properties can be removed from the `/etc/xroad.properties` file after installation (keep the other properties added by the installer).