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

Verify in the database server, that PostgreSQL package `postgresql-contrib` was installed before running following scripts:

```bash
sudo yum install postgresql-contrib
```

Run the following commands to create the necessary database structures. If necessary, customize the database and role names to suit your environment (e.g when the same database server is shared between several Security Server instances, it is necessary to have separate database names and roles for each server). By default, the database, database user, and schema use the same name (e.g. serverconf), and the admin user is named with \_admin prefix (e.g. serverconf_admin).

**serverconf** (required)
```sql
CREATE DATABASE serverconf ENCODING 'UTF8';
REVOKE ALL ON DATABASE serverconf FROM PUBLIC;
CREATE ROLE serverconf_admin LOGIN PASSWORD '<serverconf_admin password>';
GRANT serverconf_admin to <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE serverconf TO serverconf_admin;
\c serverconf
CREATE EXTENSION hstore;
CREATE SCHEMA serverconf AUTHORIZATION serverconf_admin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public to serverconf_admin;
CREATE ROLE serverconf LOGIN PASSWORD '<serverconf password>';
GRANT serverconf to <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE serverconf TO serverconf;
GRANT USAGE ON SCHEMA public to serverconf;
```

**messagelog** (required by xroad-addon-messagelog)
```sql
CREATE DATABASE messagelog ENCODING 'UTF8';
REVOKE ALL ON DATABASE messagelog FROM PUBLIC;
CREATE ROLE messagelog_admin LOGIN PASSWORD '<messagelog_admin password>';
GRANT messagelog_admin to <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE messagelog TO messagelog_admin;
\c messagelog
CREATE SCHEMA messagelog AUTHORIZATION messagelog_admin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public to messagelog_admin;
CREATE ROLE messagelog LOGIN PASSWORD '<messagelog password>';
GRANT messagelog to <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE messagelog TO messagelog;
GRANT USAGE ON SCHEMA public to messagelog;
```

**op-monitor** (optional, required by xroad-opmonitor)

If operational monitoring is going to be installed, run additionally the following commands. Again, the database and role names can be customized to suit your environment.

```sql
CREATE DATABASE "op-monitor" ENCODING 'UTF8';
REVOKE ALL ON DATABASE "op-monitor" FROM PUBLIC;
CREATE ROLE opmonitor_admin LOGIN PASSWORD '<opmonitor_admin password>';
GRANT opmonitor_admin to <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE "op-monitor" TO opmonitor_admin;
\c "op-monitor"
CREATE SCHEMA opmonitor AUTHORIZATION opmonitor_admin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public to opmonitor_admin;
CREATE ROLE opmonitor LOGIN PASSWORD '<opmonitor password>';
GRANT opmonitor to <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE "op-monitor" TO opmonitor;
GRANT USAGE ON SCHEMA public to opmonitor;
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
serverconf.database.admin_user = serverconf_admin
serverconf.database.admin_password = <serverconf_admin password>
op-monitor.database.admin_user = opmonitor_admin
op-monitor.database.admin_password = <opmonitor_admin password>
messagelog.database.admin_user = messagelog_admin
messagelog.database.admin_password = <messagelog_admin password>
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
serverconf.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/serverconf
serverconf.hibernate.connection.username = serverconf
serverconf.hibernate.connection.password = <serverconf password> 
serverconf.hibernate.hikari.dataSource.currentSchema = serverconf,public

messagelog.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/messagelog
messagelog.hibernate.connection.username = messagelog
messagelog.hibernate.connection.password = <messagelog password>
messagelog.hibernate.hikari.dataSource.currentSchema = messagelog,public

op-monitor.hibernate.connection.url = jdbc:postgresql://<database host>:<port>/op-monitor
op-monitor.hibernate.connection.username = opmonitor
op-monitor.hibernate.connection.password = <opmonitor password>
op-monitor.hibernate.hikari.dataSource.currentSchema = opmonitor,public
```