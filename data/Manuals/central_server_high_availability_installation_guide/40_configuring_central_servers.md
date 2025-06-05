### Configuring Central Servers

See [Central Server User Guide](ug-cs_x-road_6_central_server_user_guide.md#17-migrating-to-remote-database-host) for instructions about migrating an existing Central Server database to an external database.

Edit `/etc/xroad/db.properties` and change the connection properties:
```properties
spring.datasource.username=<database_user>
spring.datasource.password=<password>
spring.datasource.url=jdbc:postgresql://<master_host>:<master_port>/<database>
secondary_hosts=<standby_host>
```

Restart Central Servers and verify that the cluster is working (see [5 Monitoring HA State on a Node](#5-monitoring-ha-state-on-a-node)).