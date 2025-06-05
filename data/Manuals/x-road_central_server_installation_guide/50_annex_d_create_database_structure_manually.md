## Annex D Create Database Structure Manually

Login to the database server as the superuser (`postgres` by default).

```bash
psql -h <database host> -U <superuser> -d postgres
```

Run the following commands to create the necessary database structures and roles.
If necessary, customize the database and role names to suit your environment.
By default, the database is named `centerui_production`, database user and schema both are named `centerui`, and the admin user is named with `_admin` suffix (e.g. `centerui_admin`).


```sql
CREATE DATABASE <database> ENCODING 'UTF8';
REVOKE ALL ON DATABASE <database> FROM PUBLIC;
CREATE ROLE <admin_user> LOGIN PASSWORD '<admin_user password>';
GRANT <admin_user> TO <superuser>;
GRANT CREATE,TEMPORARY,CONNECT ON DATABASE <database> TO <admin_user>;
\c <database>
CREATE EXTENSION hstore;
CREATE SCHEMA <database_schema> AUTHORIZATION <admin_user>;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO <admin_user>;
CREATE ROLE <database_user> LOGIN PASSWORD '<database_user password>';
GRANT <database_user> TO <superuser>;
GRANT TEMPORARY,CONNECT ON DATABASE <database> TO <database_user>;
GRANT USAGE ON SCHEMA public TO <database_user>;
GRANT USAGE ON SCHEMA <database_schema> TO <database_user>;
GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA <database_schema> TO <database_user>;
GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA <database_schema> TO <database_user>;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA <database_schema> TO <database_user>;
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
centerui.database.admin_user = <admin_user>
centerui.database.admin_password = <admin_user password>
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
spring.datasource.username=<database_user>
spring.datasource.password=<database_user_password>
spring.datasource.hikari.data-source-properties.currentSchema=<database_schema>
spring.datasource.url=jdbc:postgresql://<database_host>:<database_port>/<database>
skip_migrations=<false by default, set to true to skip migrations>
```