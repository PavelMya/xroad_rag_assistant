### 1.7 High Availability Support

The High Availability (HA) solution for the X-Road Central Server relies on a shared, optionally highly available database. There can be multiple Central Server nodes each connecting to the same database instance. Furthermore, the database can be set up in high-availability mode where there is the primary node with read/write access and one or more secondary read-only nodes replicating the primary data as it changes.

In order to support high availability (HA) setup of the X-Road Central Server, some database tables have the ha_node_name field. In an HA setup, the name of the node of the cluster that initiated the insertion of a given record, is stored in that field. In ordinary setup, a default value is used. In both cases, this is done at the level of stored procedures as described in section 1.9.

The logic of taking into account the value of ha_node_name where applicable, has been implemented at the application level.

Database history records are aware of the node name in an HA setup and are replicated just like other records. Thus each node contains the full history of database changes. Because replication events happen at a lower level than insertions of records, the replication of history records themselves does not trigger any subsequent insertions of history records on target nodes.