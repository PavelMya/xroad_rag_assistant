### 19.5 Warning responses

Error response from the Management API can include additional warnings that you can ignore if seen necessary. The warnings can be ignored by your decision, by executing the same operation with `ignore_warnings` boolean parameter set to `true`. *Always consider the warning before making the decision to ignore it.*

An example case:
1. Client executes a REST request, without `ignore_warnings` parameter, to backend.
2. Backend notices warnings and responds with error message that contains the warnings. Nothing is updated at this point.
3. Client determines if warnings can be ignored.
4. If the warnings can be ignored, client resends the REST request, but with `ignore_warnings` parameter set to `true`.
5. Backend ignores the warnings and executes the operation.

Error response with warnings always contains the error code `warnings_detected`.

Like errors, warnings contain an identifier (code) and possibly some metadata.

Warning example when trying to register a WSDL that produces non-fatal validation warnings:
```json
{
  "status": 400,
  "error": {
    "code": "warnings_detected"
  },
  "warnings": [
    {
      "code": "wsdl_validation_warnings",
      "metadata": [
        "WSDLValidator Error : Summary: Failures: 0, Warnings: 1  -p  -U postgres
    CREATE DATABASE serverconf ENCODING 'UTF8';
    REVOKE ALL ON DATABASE serverconf FROM PUBLIC;
    CREATE ROLE serverconf_admin LOGIN PASSWORD '';
    GRANT serverconf_admin to ;
    GRANT CREATE,TEMPORARY,CONNECT ON DATABASE serverconf TO serverconf_admin;
    \c serverconf
    CREATE EXTENSION hstore;
    CREATE SCHEMA serverconf AUTHORIZATION serverconf_admin;
    REVOKE ALL ON SCHEMA public FROM PUBLIC;
    GRANT USAGE ON SCHEMA public to serverconf_admin;
    CREATE ROLE serverconf LOGIN PASSWORD '';
    GRANT serverconf to ;
    GRANT TEMPORARY,CONNECT ON DATABASE serverconf TO serverconf;
    GRANT USAGE ON SCHEMA public to serverconf;
    GRANT USAGE ON SCHEMA serverconf TO serverconf;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA serverconf TO serverconf;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA serverconf TO serverconf;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA serverconf to serverconf;
    ```

    **messagelog** (required by xroad-addon-messagelog)
    ```bash
    psql -h  -p  -U postgres
    CREATE DATABASE messagelog ENCODING 'UTF8';
    REVOKE ALL ON DATABASE messagelog FROM PUBLIC;
    CREATE ROLE messagelog_admin LOGIN PASSWORD '';
    GRANT messagelog_admin to ;
    GRANT CREATE,TEMPORARY,CONNECT ON DATABASE messagelog TO messagelog_admin;
    \c messagelog
    CREATE SCHEMA messagelog AUTHORIZATION messagelog_admin;
    REVOKE ALL ON SCHEMA public FROM PUBLIC;
    GRANT USAGE ON SCHEMA public to messagelog_admin;
    CREATE ROLE messagelog LOGIN PASSWORD '';
    GRANT messagelog to ;
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
    psql -h  -p  -U postgres
    CREATE DATABASE "op-monitor" ENCODING 'UTF8';
    REVOKE ALL ON DATABASE "op-monitor" FROM PUBLIC;
    CREATE ROLE opmonitor_admin LOGIN PASSWORD '';
    GRANT opmonitor_admin to ;
    GRANT CREATE,TEMPORARY,CONNECT ON DATABASE "op-monitor" TO opmonitor_admin;
    \c "op-monitor"
    CREATE SCHEMA opmonitor AUTHORIZATION opmonitor_admin;
    REVOKE ALL ON SCHEMA public FROM PUBLIC;
    GRANT USAGE ON SCHEMA public to opmonitor_admin;
    CREATE ROLE opmonitor LOGIN PASSWORD '';
    GRANT opmonitor to ;
    GRANT TEMPORARY,CONNECT ON DATABASE "op-monitor" TO opmonitor;
    GRANT USAGE ON SCHEMA public to opmonitor;
    GRANT USAGE ON SCHEMA opmonitor TO opmonitor;
    GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA opmonitor TO opmonitor;
    GRANT SELECT,UPDATE ON ALL SEQUENCES IN SCHEMA opmonitor TO opmonitor;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA opmonitor to opmonitor;
    ```

5. Restore the database dumps on the remote database host.

    ```bash
    pg_restore -h  -p  -U serverconf_admin -O -n serverconf -1 -d serverconf serverconf.dat
    pg_restore -h  -p  -U messagelog_admin -O -n messagelog -1 -d messagelog messagelog.dat
    pg_restore -h  -p  -U opmonitor_admin -O -n opmonitor -1 -d op-monitor op-monitor.dat
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
    serverconf.database.admin_password = 
    messagelog.database.admin_user = messagelog_admin
    messagelog.database.admin_password = messagelog_admin password>
    op-monitor.database.admin_user = opmonitor_admin
    op-monitor.database.admin_password = 
    ```

8. Update `/etc/xroad/db.properties` contents with correct database host URLs and passwords.

    ```properties
    serverconf.hibernate.connection.url = jdbc:postgresql://:/serverconf
    serverconf.hibernate.connection.username = serverconf
    serverconf.hibernate.connection.password = 
    serverconf.hibernate.hikari.dataSource.currentSchema = serverconf,public

    messagelog.hibernate.connection.url = jdbc:postgresql://:/messagelog
    messagelog.hibernate.connection.username = messagelog
    messagelog.hibernate.connection.password = 
    messagelog.hibernate.hikari.dataSource.currentSchema = messagelog,public

    op-monitor.hibernate.connection.url = jdbc:postgresql://:/op-monitor
    op-monitor.hibernate.connection.username = opmonitor
    op-monitor.hibernate.connection.password = 
    op-monitor.hibernate.hikari.dataSource.currentSchema = opmonitor,public
    ```

9. Start again the X-Road services.

    ```bash
    systemctl start "xroad*"
    ```