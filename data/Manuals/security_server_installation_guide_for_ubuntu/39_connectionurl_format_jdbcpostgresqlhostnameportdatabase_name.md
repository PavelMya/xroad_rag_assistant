# connection.url format: jdbc:postgresql://<hostname>:<port>/<database name>

serverconf.hibernate.connection.url = jdbc:postgresql://127.0.0.1:5432/serverconf
serverconf.hibernate.connection.username = serverconf
serverconf.hibernate.connection.password = <randomly generated password>
serverconf.hibernate.connection.driver_class = org.postgresql.Driver
serverconf.hibernate.dialect = ee.ria.xroad.common.db.CustomPostgreSQLDialect
serverconf.hibernate.hikari.dataSource.currentSchema = serverconf,public
serverconf.hibernate.jdbc.use_streams_for_binary = true

messagelog.hibernate.connection.url = jdbc:postgresql://127.0.0.1:5432/messagelog
messagelog.hibernate.connection.username = messagelog
messagelog.hibernate.connection.password = <randomly generated password>
messagelog.hibernate.connection.driver_class = org.postgresql.Driver
messagelog.hibernate.dialect = ee.ria.xroad.common.db.CustomPostgreSQLDialect
messagelog.hibernate.hikari.dataSource.currentSchema = messagelog,public
messagelog.hibernate.jdbc.use_streams_for_binary = true

op-monitor.hibernate.connection.url = jdbc:postgresql://127.0.0.1:5432/op-monitor
op-monitor.hibernate.connection.username = opmonitor
op-monitor.hibernate.connection.password = <randomly generated password>
op-monitor.hibernate.connection.driver_class = org.postgresql.Driver
op-monitor.hibernate.hikari.dataSource.currentSchema = opmonitor,public
op-monitor.hibernate.jdbc.use_streams_for_binary = true
```