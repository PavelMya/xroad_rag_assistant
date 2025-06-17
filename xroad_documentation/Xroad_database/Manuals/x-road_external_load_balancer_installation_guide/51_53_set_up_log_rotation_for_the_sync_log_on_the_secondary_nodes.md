### 5.3 Set up log rotation for the sync log on the secondary nodes

The configuration synchronization will log events to `/var/log/xroad/slave-sync.log` on the secondary nodes. The following
configuration example rotates those logs daily and keeps them for 7 days which should be enough for troubleshooting.

Create a new file `/etc/logrotate.d/xroad-slave-sync` on the secondary nodes:

```
/var/log/xroad/slave-sync.log {
        daily
        rotate 7
        missingok
        compress
        su xroad xroad
        nocreate
}
```

## 6. Verifying the setup

This chapter briefly describes how to check that the replication works. Message delivery is difficult to test without a
connection to an X-Road instance test environment.