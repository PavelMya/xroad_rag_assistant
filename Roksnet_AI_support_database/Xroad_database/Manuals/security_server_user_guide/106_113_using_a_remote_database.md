### 11.3 Using a Remote Database

The message log database can be located outside of the Security Server. The following guide describes how to configure and populate a remote database schema for the message log. It is assumed that access to the database from the Security Server has been configured. For detailed information about the configuration of database connections, refer to \[[JDBC](#Ref_JDBC)\].

1.  Create a database user at remote database host:

        postgres@db_host:~$ createuser -P messagelog_user
        Enter password for new role: 
        Enter it again: 

2.  Create a database owned by the message log user at remote database host:

        postgres@db_host:~$ createdb messagelog_dbname -O messagelog_user -E UTF-8

3.  Verify connectivity from Security Server to the remote database:

        user@security_server:~$ psql -h db_host -U messagelog_user messagelog_dbname
        Password for user messagelog_user: 
        psql (9.3.9)
        SSL connection (cipher: DHE-RSA-AES256-GCM-SHA384, bits: 256)
        Type "help" for help.
        messagelog_dbname=>

4.  Stop xroad-proxy service for reconfiguration:

        root@security_server:~# service xroad-proxy stop

5.  Configure the database connection parameters to achieve encrypted connections, in `/etc/xroad/db.properties`:

        messagelog.hibernate.jdbc.use_streams_for_binary = true
        messagelog.hibernate.dialect = ee.ria.xroad.common.db.CustomPostgreSQLDialect
        messagelog.hibernate.connection.driver_class = org.postgresql.Driver
        messagelog.hibernate.connection.url = jdbc:postgresql://db_host:5432/messagelog_dbname?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory
        messagelog.hibernate.connection.username = messagelog_user
        messagelog.hibernate.connection.password = messagelog_password

6.  Populate database schema by reinstalling messagelog addon package and start xroad-proxy

    Ubuntu: `apt-get install --reinstall xroad-addon-messagelog`  
    RHEL: `yum reinstall xroad-addon-messagelog`

    `service xroad-proxy start`