## Annex D Create Database Structure Manually

Depending on installed components, the Security Server uses one to three databases (catalogs):

* _serverconf_ for storing Security Server configuration (required)
* _messagelog_ for storing message records (optional, but installed by default)
* _op-monitor_ for operational monitoring data (optional)

These databases can be hosted on one database server (default setup), or you can use several servers. 

Login to the database server(s) as the superuser (`postgres` by default) to run the commands, e.g.
```bash
psql -h : -U  -d postgres
```

Run the following commands to create the necessary database structures.
If necessary, customize the database and role names to suit your environment (e.g when the same database server is shared between several Security Server instances, it is necessary to have separate database names and roles for each server).

**serverconf** (required)

By default, the database, database user, and schema use the same name of `serverconf`, and the admin user is named with `_admin` suffix (e.g. `serverconf_admin`).

```sql
CREATE DATABASE  ENCODING 'UTF8';
REVOKE ALL ON DATABASE  FROM PUBLIC;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE  TO ;
\c 
CREATE EXTENSION hstore;
CREATE SCHEMA  AUTHORIZATION ;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO ;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT TEMPORARY,CONNECT ON DATABASE  TO ;
GRANT USAGE ON SCHEMA public TO ;
GRANT USAGE ON SCHEMA  TO ;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA  TO ;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA  TO ;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA  TO ;
```

**messagelog** (required by xroad-addon-messagelog)

By default, the database, database user, and schema use the same name of `messagelog`, and the admin user is named with `_admin` suffix (e.g. `messagelog_admin`).

```sql
CREATE DATABASE  ENCODING 'UTF8';
REVOKE ALL ON DATABASE  FROM PUBLIC;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE  TO ;
\c 
CREATE SCHEMA  AUTHORIZATION ;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO ;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT TEMPORARY,CONNECT ON DATABASE  TO ;
GRANT USAGE ON SCHEMA public TO ;
GRANT USAGE ON SCHEMA  TO ;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA  TO ;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA  TO ;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA  TO ;
```

**op-monitor** (optional, required by xroad-opmonitor)

If operational monitoring is going to be installed, run additionally the following commands. Again, the database and role names can be customized to suit your environment.
By default, the database is named `op-monitor`, database user and schema both are named `opmonitor`, and the admin user is named with `_admin` suffix (e.g. `opmonitor_admin`).

```sql
CREATE DATABASE  ENCODING 'UTF8';
REVOKE ALL ON DATABASE  FROM PUBLIC;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE  TO ;
\c 
CREATE SCHEMA  AUTHORIZATION ;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO ;
CREATE ROLE  LOGIN PASSWORD '';
GRANT  TO ;
GRANT TEMPORARY,CONNECT ON DATABASE  TO ;
GRANT USAGE ON SCHEMA public TO ;
GRANT USAGE ON SCHEMA  TO ;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA  TO ;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA  TO ;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA  TO ;
```

Lastly, customize the database connection properties to match the values used when creating the database.

Note. When using Microsoft Azure PostgreSQL, the user names need to be in format `username@hostname` in the properties files.

Create the configuration file `/etc/xroad.properties`.
```bash
sudo touch /etc/xroad.properties
sudo chown root:root /etc/xroad.properties
sudo chmod 600 /etc/xroad.properties
```

Edit `/etc/xroad.properties` and add/update the following properties (if you customized the role names, use your own). The admin users are used to run database migrations during the install and upgrades.
```properties
serverconf.database.admin_user = 
serverconf.database.admin_password = 
messagelog.database.admin_user = 
messagelog.database.admin_password = 
op-monitor.database.admin_user = 
op-monitor.database.admin_password = 
```

Create the `/etc/xroad/db.properties` file
```bash
sudo mkdir /etc/xroad
sudo chown xroad:xroad /etc/xroad
sudo chmod 751 /etc/xroad
sudo touch /etc/xroad/db.properties
sudo chmod 0640 /etc/xroad/db.properties
sudo chown xroad:xroad /etc/xroad/db.properties
```

Edit the `/etc/xroad/db.properties` file and add/update the following connection properties (if you customized the database, user, and/or role names, use the customized values).
The database connection url format is `jdbc:postgresql://:/`
```properties
serverconf.hibernate.connection.url = jdbc:postgresql://:/
serverconf.hibernate.connection.username = 
serverconf.hibernate.connection.password = 
serverconf.hibernate.hikari.dataSource.currentSchema = ,public

messagelog.hibernate.connection.url = jdbc:postgresql://:/
messagelog.hibernate.connection.username = 
messagelog.hibernate.connection.password = 
messagelog.hibernate.hikari.dataSource.currentSchema = ,public

op-monitor.hibernate.connection.url = jdbc:postgresql://:/
op-monitor.hibernate.connection.username = 
op-monitor.hibernate.connection.password = 
op-monitor.hibernate.hikari.dataSource.currentSchema = ,public
```