### Configuring Central Servers

See [Central Server User Guide](ug-cs_x-road_6_central_server_user_guide.md#17-migrating-to-remote-database-host) for instructions about migrating an existing Central Server database to an external database.

Edit `/etc/xroad/db.properties` and change the connection properties:
```properties
spring.datasource.username=
spring.datasource.password=
spring.datasource.url=jdbc:postgresql://:/
secondary_hosts=
```

Restart Central Servers and verify that the cluster is working (see [5 Monitoring HA State on a Node](#5-monitoring-ha-state-on-a-node)).

### Fail-over

In case the master server fails, one can manually promote the standby to a master by executing the following command on the standby server:
```bash
sudo pg_ctl promote
```

On Ubuntu pg_ctl is typically not in the path, use pg_ctlcluster instead:
```bash
sudo pg_ctlcluster   promote