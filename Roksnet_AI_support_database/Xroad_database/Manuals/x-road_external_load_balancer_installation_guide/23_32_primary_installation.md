### 3.2 Primary installation

1. Install the X-Road Security Server packages using the normal installation procedure or use an existing standalone node.
2. Stop the xroad services.
3. Create a separate PostgreSQL instance for the `serverconf` database (see section
   [4. Database replication setup](#4-database-replication-setup) for details).
4. Change `/etc/xroad/db.properties` to point to the separate database instance:
   * `serverconf.hibernate.connection.url` : Change the url port number from `5432` to `5433` (or the port you specified)
5. If you are using an already configured server as the primary, the existing configuration was replicated to the secondaries
   in step 3. Otherwise, proceed to configure the primary server: install the configuration anchor, set up basic information,
   create authentication and signing keys and so on. See the Security Server installation guide \[[IG-SS](#13-references)\]
   for help with the basic setup.
6. Set up the configuration file replication, see section
   [5. Configuring data replication with rsync over SSH](#5-configuring-data-replication-with-rsync-over-ssh)
   * Additionally, `rssh` shell can be used to restrict secondary access further, but note that it is not available on RHEL.

7. Configure the node type as `master` in `/etc/xroad/conf.d/node.ini`:
      ```ini
      [node]
      type=master
      ```
      Change the owner and group of the file to `xroad:xroad` if it is not already.
8. Disable support for client-side pooled connections (HTTP connection persistence) in `/etc/xroad/conf.d/local.ini`
    * Because the load balancing works at TCP level, disabling persistent HTTP connections is recommended so that the load balancer can evenly distribute the traffic.
      ```ini
      [proxy]
      server-support-clients-pooled-connections=false
      ```
9. Start the X-Road services.