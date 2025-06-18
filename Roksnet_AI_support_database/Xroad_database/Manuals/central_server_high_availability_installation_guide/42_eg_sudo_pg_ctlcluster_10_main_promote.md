# e.g. sudo pg_ctlcluster 10 main promote
```

If the standby is configured as a secondary database host on the Central Servers, the servers will automatically reconnect to it.
To avoid a "split-brain" situation, the old master must not be started until it has been reconfigured as a standby.

See also: https://www.postgresql.org/docs/current/warm-standby-failover.html