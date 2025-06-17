#### 2.1.2 Consequences of the selected implementation model
* Changes to the `serverconf` database, authorization and signing keys are applied via the configuration primary, which is
  a member of the cluster. The replication is one-way from primary to secondaries and the secondaries should treat the configuration
  as read-only.
* The cluster nodes can continue operation if the primary fails but the configuration can not be changed until:
  - the primary comes back online, or
  - some other node is manually promoted to be the primary.
* If a node fails, the messages being processed by that node are lost.
  - It is the responsibility of the load balancer component to detect the failure and route further messages to other nodes.
    Because there potentially is some delay before the failure is noticed, some messages might be lost due to the delay.
  - Recovering lost messages is not supported.
* Configuration updates are asynchronous and the cluster state is eventually consistent.
* If the primary node fails or communication is interrupted during a configuration update, each secondary should have a valid
  configuration, but the cluster state can be inconsistent (some members might have the old configuration while some might
  have received all the changes).