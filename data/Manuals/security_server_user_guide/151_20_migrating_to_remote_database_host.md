## 20 Migrating to Remote Database Host

Since version `6.22.0` Security Server supports using remote databases. In case you have an already running Security Server with local database, it is possible to migrate it to use remote database host instead. The instructions for this process are listed below.

1. Shutdown X-Road processes.

    ```bash
    systemctl stop "xroad*"
    ```

2. Dump the local databases to be migrated. You can find the passwords of users `serverconf_admin`, `messagelog_admin` and `opmonitor_admin` in `/etc/xroad.properties`.Notice that the versions of the local PostgreSQL client and remote PostgreSQL server must match. Also take into account that on a busy system the messagelog database can be quite large and therefore dump and restore can take considerable amount of time and disk space. Notice that the versions of the local PostgreSQL client and remote PostgreSQL server must match.

    ```bash
    pg_dump -F t -h 127.0.0.1 -p 5432 -U serverconf_admin -f serverconf.dat serverconf
    pg_dump -F t -h 127.0.0.1 -p 5432 -U messagelog_admin -f messagelog.dat messagelog
    pg_dump -F t -h 127.0.0.1 -p 5432 -U opmonitor_admin -f op-monitor.dat op-monitor
    ```

3. Shut down and mask local `postgresql` so it won't start when `xroad-proxy` starts.

    ```bash
    systemctl stop postgresql
    systemctl mask postgresql
    ```

4. Connect to the remote database server as the superuser `postgres` and create roles, databases and access permissions as follows.

    **serverconf** (required)
    ```bash
    psql -h <remote-db-url> -p <remote-db-port> -U postgres
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
    GRANT USAGE ON SCHEMA serverconf TO serverconf;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA serverconf TO serverconf;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA serverconf TO serverconf;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA serverconf to serverconf;
    ```

    **messagelog** (required by xroad-addon-messagelog)
    ```bash
    psql -h <remote-db-url> -p <remote-db-port> -U postgres
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
    GRANT USAGE ON SCHEMA messagelog TO messagelog;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA messagelog TO messagelog;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA messagelog TO messagelog;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA messagelog to messagelog;
    ```

    **op-monitor** (optional, required by xroad-opmonitor)

    If operational monitoring is going to be installed, run additionally the following commands. Again, the database and role names can be customized to suit your environment.

    ```bash
    psql -h <remote-db-url> -p <remote-db-port> -U postgres
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
    GRANT USAGE ON SCHEMA opmonitor TO opmonitor;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA opmonitor TO opmonitor;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA opmonitor TO opmonitor;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA opmonitor to opmonitor;
    ```

5. Restore the database dumps on the remote database host.

    ```bash
    pg_restore -h <remote-db-url> -p <remote-db-port> -U serverconf_admin -O -n serverconf -1 -d serverconf serverconf.dat
    pg_restore -h <remote-db-url> -p <remote-db-port> -U messagelog_admin -O -n messagelog -1 -d messagelog messagelog.dat
    pg_restore -h <remote-db-url> -p <remote-db-port> -U opmonitor_admin -O -n opmonitor -1 -d op-monitor op-monitor.dat
    ```

6. Create properties file `/etc/xroad.properties` containing the superuser password.

    ```bash
    sudo touch /etc/xroad.properties
    sudo chown root:root /etc/xroad.properties
    sudo chmod 600 /etc/xroad.properties
    ```

7. Edit `/etc/xroad.properties`.

    ```properties
    serverconf.database.admin_user = serverconf_admin
    serverconf.database.admin_password = <serverconf_admin password>
    messagelog.database.admin_user = messagelog_admin
    messagelog.database.admin_password = messagelog_admin password>
    op-monitor.database.admin_user = opmonitor_admin
    op-monitor.database.admin_password = <opmonitor_admin password>
    ```

8. Update `/etc/xroad/db.properties` contents with correct database host URLs and passwords.

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

9. Start again the X-Road services.

    ```bash
    systemctl start "xroad*"
    ```