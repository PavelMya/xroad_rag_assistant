### 2.6 Remote Database Setup (optional)

*This is an optional step.* 

Optionally, the Central Server can use a remote database server. To avoid installing the default local PostgreSQL server during the installation, first install the `xroad-database-remote` -package.
```bash
sudo apt install xroad-database-remote
```

For the application level backup and restore feature to work correctly, it is important to verify that the local PostgreSQL client has the same or later major version than the remote database server and, if necessary, install a different version of the `postgresql-client` package (see https://www.postgresql.org/download/linux/ubuntu/)
```bash
psql --version
psql (PostgreSQL) 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)

psql -h  -U  -tAc 'show server_version'
10.16 (Ubuntu 10.16-0ubuntu0.18.04.1)
```

The installer can create the database and users for you, but you need to create a configuration file containing the database administrator credentials. 

For advanced setup, e.g. if storing the database administrator password on the server is not an option, you can create the database users and structure manually as described in [Annex D Create Database Structure Manually](#annex-d-create-database-structure-manually) and then continue to section 2.7. 

For setting up a database connection with SSL certificates, you need to create an additional configuration file `db_libpq.env` in the `/etc/xroad/` folder. For more details see the section „Passing additional parameters to psql“ in [UG-CS](#Ref_UG-CS).

When leaving the database and user creation to the installer, continue with the following steps:

Create the property file:
```bash
sudo touch /etc/xroad.properties
sudo chown root:root /etc/xroad.properties
sudo chmod 600 /etc/xroad.properties
```

Edit `/etc/xroad.properties`. See the example below. Replace parameter values with your own.
```properties
postgres.connection.password = 
postgres.connection.user = 
```

Note. If Microsoft Azure database for PostgreSQL is used, the connection user needs to be in format `username@hostname`.

For additional security, the `postgresql.connection.*` properties can be removed from the `/etc/xroad.properties` file after installation (keep the other properties added by the installer).

Before continuing, test that the connection to the database works, e.g.
```bash
psql -h  -U  -tAc 'show server_version'
```