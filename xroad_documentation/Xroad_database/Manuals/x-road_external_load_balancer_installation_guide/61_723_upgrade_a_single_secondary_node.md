#### 7.2.3 Upgrade a single secondary node

Repeat this process for each secondary node, one by one.

1. Gracefully disable the secondary node from the load balancer, either manually or using the health check maintenance mode.
   See [step 1 from the primary update instructions](#primary-upgrade-step-1) for more details.

2. Stop the X-Road services once the secondary has stopped processing requests. See [step 2 from the primary update instructions](#primary-upgrade-step-2)
   for more details.

3. Enable database synchronization on the secondary:
   ```bash
   #PostgreSQL version = 10
   sudo -u postgres psql -p 5433 -c 'select pg_wal_replay_resume()'
   ```
   Note that the above command assumes that the `serverconf` database is running in port `5433`.

   **Note:** Before proceeding, make sure that the database is up to date. The following should return `t`:
   ```bash
   #PostgreSQL = 10
   sudo -u postgres psql -p 5433 -c 'select pg_last_wal_replay_lsn() = pg_last_wal_receive_lsn()'
   ```
4. Upgrade the packages on the secondary node to the new software version.

5. Enable the shared configuration synchronization on the secondary node:
   ```bash
   sudo rm /var/tmp/xroad/sync-disabled
   ```
6. Wait for the primary node configuration changes to propagate to the secondary node.

   The configuration synchronization can be forced, if necessary.

   ```bash
   service xroad-sync start
   ```
   
7. Restart the X-Road services and wait until the secondary node is healthy.

8. After the node is healthy, enable the secondary node in the load balancer if you manually disabled it. If using the
   maintenance mode, it was cleared on `xroad-proxy` service restart. See
   [step 5 from the primary update instructions](#primary-upgrade-step-5) for more details.