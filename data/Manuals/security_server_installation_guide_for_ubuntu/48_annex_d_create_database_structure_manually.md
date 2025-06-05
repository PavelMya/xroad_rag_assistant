## Annex D Create Database Structure Manually

Depending on installed components, the Security Server uses one to three databases (catalogs):

* _serverconf_ for storing Security Server configuration (required)
* _messagelog_ for storing message records (optional, but installed by default)
* _op-monitor_ for operational monitoring data (optional)

These databases can be hosted on one database server (default setup), or you can use several servers. 

Login to the database server(s) as the superuser (`postgres` by default) to run the commands, e.g.
```bash
psql -h <database host>:<port> -U <superuser> -d postgres
```

Run the following commands to create the necessary database structures.
If necessary, customize the database and role names to suit your environment (e.g when the same database server is shared between several Security Server instances, it is necessary to have separate database names and roles for each server).

**serverconf** (required)

By default, the database, database user, and schema use the same name of `serverconf`, and the admin user is named with `_admin` suffix (e.g. `serverconf_admin`).

```sql
CREATE DATABASE <serverconf_database> ENCODING 'UTF8';
REVOKE ALL ON DATABASE <serverconf_database> FROM PUBLIC;
CREATE ROLE <serverconf_admin_user> LOGIN PASSWORD '<serverconf_admin_user password>';
GRANT <serverconf_admin_user> TO <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE <serverconf_database> TO <serverconf_admin_user>;
\c <serverconf_database>
CREATE EXTENSION hstore;
CREATE SCHEMA <serverconf_schema> AUTHORIZATION <serverconf_admin_user>;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO <serverconf_admin_user>;
CREATE ROLE <serverconf_database_user> LOGIN PASSWORD '<serverconf_database_user password>';
GRANT <serverconf_database_user> TO <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE <serverconf_database> TO <serverconf_database_user>;
GRANT USAGE ON SCHEMA public TO <serverconf_database_user>;
GRANT USAGE ON SCHEMA <serverconf_schema> TO <serverconf_database_user>;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA <serverconf_schema> TO <serverconf_database_user>;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA <serverconf_schema> TO <serverconf_database_user>;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA <serverconf_schema> TO <serverconf_database_user>;
```

**messagelog** (required by xroad-addon-messagelog)

By default, the database, database user, and schema use the same name of `messagelog`, and the admin user is named with `_admin` suffix (e.g. `messagelog_admin`).

```sql
CREATE DATABASE <messagelog_database> ENCODING 'UTF8';
REVOKE ALL ON DATABASE <messagelog_database> FROM PUBLIC;
CREATE ROLE <messagelog_admin_user> LOGIN PASSWORD '<messagelog_admin_user password>';
GRANT <messagelog_admin_user> TO <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE <messagelog_database> TO <messagelog_admin_user>;
\c <messagelog_database>
CREATE SCHEMA <messagelog_schema> AUTHORIZATION <messagelog_admin_user>;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO <messagelog_admin_user>;
CREATE ROLE <messagelog_database_user> LOGIN PASSWORD '<messagelog_database_user password>';
GRANT <messagelog_database_user> TO <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE <messagelog_database> TO <messagelog_database_user>;
GRANT USAGE ON SCHEMA public TO <messagelog_database_user>;
GRANT USAGE ON SCHEMA <messagelog_schema> TO <messagelog_database_user>;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA <messagelog_schema> TO <messagelog_database_user>;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA <messagelog_schema> TO <messagelog_database_user>;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA <messagelog_schema> TO <messagelog_database_user>;
```

**op-monitor** (optional, required by xroad-opmonitor)

If operational monitoring is going to be installed, run additionally the following commands. Again, the database and role names can be customized to suit your environment.
By default, the database is named `op-monitor`, database user and schema both are named `opmonitor`, and the admin user is named with `_admin` suffix (e.g. `opmonitor_admin`).

```sql
CREATE DATABASE <opmonitor_database> ENCODING 'UTF8';
REVOKE ALL ON DATABASE <opmonitor_database> FROM PUBLIC;
CREATE ROLE <opmonitor_admin_user> LOGIN PASSWORD '<opmonitor_admin_user password>';
GRANT <opmonitor_admin_user> TO <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE <opmonitor_database> TO <opmonitor_admin_user>;
\c <opmonitor_database>
CREATE SCHEMA <opmonitor_schema> AUTHORIZATION <opmonitor_admin_user>;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO <opmonitor_admin_user>;
CREATE ROLE <database_user> LOGIN PASSWORD '<opmonitor_database_user password>';
GRANT <opmonitor_database_user> TO <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE <opmonitor_database> TO <opmonitor_database_user>;
GRANT USAGE ON SCHEMA public TO <opmonitor_database_user>;
GRANT USAGE ON SCHEMA <opmonitor_schema> TO <opmonitor_database_user>;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA <opmonitor_schema> TO <opmonitor_database_user>;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA <opmonitor_schema> TO <opmonitor_database_user>;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA <opmonitor_schema> TO <opmonitor_database_user>;
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
serverconf.database.admin_user = <serverconf_admin_user>
serverconf.database.admin_password = <serverconf_admin_user password>
messagelog.database.admin_user = <messagelog_admin_user>
messagelog.database.admin_password = <messagelog_admin_user password>
op-monitor.database.admin_user = <opmonitor_admin_user>
op-monitor.database.admin_password = <opmonitor_admin_user password>
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
The database connection url format is `jdbc:postgresql://<database host>:<port>/<database name>`
```properties
serverconf.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/<serverconf_database>
serverconf.hibernate.connection.username = <serverconf_database_user>
serverconf.hibernate.connection.password = <serverconf_database_user password>
serverconf.hibernate.hikari.dataSource.currentSchema = <serverconf_schema>,public

messagelog.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/<messagelog_database>
messagelog.hibernate.connection.username = <messagelog_database_user>
messagelog.hibernate.connection.password = <messagelog_database_user password>
messagelog.hibernate.hikari.dataSource.currentSchema = <messagelog_schema>,public

op-monitor.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/<opmonitor_database>
op-monitor.hibernate.connection.username = <opmonitor_database_user>
op-monitor.hibernate.connection.password = <opmonitor_database_user password>
op-monitor.hibernate.hikari.dataSource.currentSchema = <opmonitor_schema>,public
```