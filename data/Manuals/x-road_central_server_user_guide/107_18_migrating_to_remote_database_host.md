## 18. Migrating to Remote Database Host

Since version 6.23.0 Central Server supports using remote databases. In case you have an already running standalone Central Server with local database, it is possible to migrate it to use remote database host instead. The instructions for this process are listed below.

Prerequisites

* Same version (12 or later) of PostgreSQL installed on the remote database host.
* Network connections to PostgreSQL port (tcp/5432) are allowed from the Central Server to the remote database server.

1. Shutdown X-Road processes.

```bash
systemctl stop "xroad*"
```

2. Dump the local database centerui_production to be migrated. The credentials of the database admin user can be found in `/etc/xroad.properties`. Notice that the versions of the local PostgreSQL client and remote PostgreSQL server must match.

```bash
pg_dump -F t -h 127.0.0.1 -p 5432 -U centerui_admin -f centerui_production.dat centerui_production
```

3. Shut down and mask local postgresql so it won't start when xroad-proxy starts.

```bash
systemctl stop postgresql
```

```bash
systemctl mask postgresql
```

4. Connect to the remote database server as the superuser postgres and create roles, databases and access permissions as follows.

```bash
    psql -h <remote-db-url> -p <remote-db-port> -U postgres
    CREATE DATABASE centerui_production ENCODING 'UTF8';
    REVOKE ALL ON DATABASE centerui_production FROM PUBLIC;
    CREATE ROLE centerui_admin LOGIN PASSWORD '<centerui_admin password>';
    GRANT centerui_admin TO postgres;
    GRANT CREATE,TEMPORARY,CONNECT ON DATABASE centerui_production TO centerui_admin;
    \c centerui_production
    CREATE EXTENSION hstore;
    CREATE SCHEMA centerui AUTHORIZATION centerui_admin;
    REVOKE ALL ON SCHEMA public FROM PUBLIC;
    GRANT USAGE ON SCHEMA public TO centerui_admin;
    CREATE ROLE centerui LOGIN PASSWORD '<centerui password>';
    GRANT centerui TO postgres;
    GRANT TEMPORARY,CONNECT ON DATABASE centerui_production TO centerui;
    GRANT USAGE ON SCHEMA public TO centerui;
    GRANT USAGE ON SCHEMA centerui TO centerui;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA centerui TO centerui;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA centerui TO centerui;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA centerui to centerui;
```

5. Restore the database dumps on the remote database host.

```bash
pg_restore -h <remote-db-url> -p <remote-db-port> -U centerui_admin -O -n centerui -1 -d centerui_production centerui_production.dat
```

6. Create properties file `/etc/xroad.properties` if it does not exist.

```bash
    sudo touch /etc/xroad.properties
    sudo chown root:root /etc/xroad.properties
    sudo chmod 600 /etc/xroad.properties
```

7. Make sure `/etc/xroad.properties` is containing the admin user & its password.

```properties
    centerui.database.admin_user = centerui_admin
    centerui.database.admin_password = <centerui_admin password>
```

8. Update `/etc/xroad/db.properties` contents with correct database host URLs and passwords.

```properties
    spring.datasource.username=<database_username>
    spring.datasource.password=<database_password>
    spring.datasource.hikari.data-source-properties.currentSchema=<database_schema>
    spring.datasource.url=jdbc:postgresql://<database_host>:<database_port>/<database>
```

9. Start again the X-Road services.

```bash
systemctl start "xroad*"
```