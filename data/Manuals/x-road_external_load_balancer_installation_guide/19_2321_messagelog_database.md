##### 2.3.2.1 `messagelog` database

The messagelog database is not replicated. Each node has its own separate messagelog database. **However**, in order to
support PostgreSQL streaming replication (hot standby mode) for the serverconf data, the serverconf and messagelog
databases must be separated. This requires modifications to the installation (a separate PostgreSQL instance is needed
for the messagelog database) and has some implications on the Security Server resource requirements as a separate
instance uses some memory.