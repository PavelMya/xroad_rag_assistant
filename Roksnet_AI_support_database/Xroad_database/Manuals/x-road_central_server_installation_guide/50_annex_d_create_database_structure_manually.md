## Annex D Create Database Structure Manually

Login to the database server as the superuser (`postgres` by default).

```bash
psql -h  -U  -d postgres
```

Run the following commands to create the necessary database structures and roles.
If necessary, customize the database and role names to suit your environment.
By default, the database is named `centerui_production`, database user and schema both are named `centerui`, and the admin user is named with `_admin` suffix (e.g. `centerui_admin`).


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

Create the `/etc/xroad.properties` file
```bash
sudo touch /etc/xroad.properties
sudo chown root:root /etc/xroad.properties
sudo chmod 0600 /etc/xroad.properties
```

Edit `/etc/xroad.properties` and add/update the following properties (if you customized the role names, use your own).
The admin users are used to run database migrations during the install and upgrades.

```properties
centerui.database.admin_user = 
centerui.database.admin_password = 
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

Edit `/etc/xroad/db.properties` file and add/update the following connection properties (if you customized the database, user, and/or role names, use the customized values).
The default values can be found in [Annex A Central Server Default Database Properties](#annex-a-central-server-default-database-properties).

```properties
spring.datasource.username=
spring.datasource.password=
spring.datasource.hikari.data-source-properties.currentSchema=
spring.datasource.url=jdbc:postgresql://:/
skip_migrations=
```