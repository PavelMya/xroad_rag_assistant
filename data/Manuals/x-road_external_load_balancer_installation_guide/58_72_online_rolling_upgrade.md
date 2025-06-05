### 7.2 Online rolling upgrade
It is possible to upgrade the software in a cluster to a new version with minimal service disruption.

The steps are in more detail below, but in short, the procedure is:

1. Pause the database and configuration synchronization on the secondary nodes. Pausing the synchronization ensures that
   potentially incompatible changes are not propagated to secondaries before they are upgraded.
2. Set the primary node to maintenance mode or manually disable it from the external load balancer, upgrade the software,
   then resume operation.
3. One by one, set a secondary node to maintenance mode or manually disable it from the external load balancer, re-enable
   synchronization, upgrade it, then resume operation.