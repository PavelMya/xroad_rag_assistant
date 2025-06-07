### 6.1 Verifying rsync+ssh replication

To test the configuration file replication, a new file can be added to `/etc/xroad/` or `/etc/xroad/signer/` on the
primary node and verify it has been replicated to the secondary nodes in a few minutes. Make sure the file is owned by
the group `xroad`.

Alternatively, check the sync log `/var/log/xroad/slave-sync.log` on the secondary nodes and verify it lists successful
transfers. A transfer of an added test file called `sync.testfile` to `/etc/xroad/signer/` might look like this:

```
2017/03/10 11:42:01 [10505] receiving file list
2017/03/10 11:42:01 [10507] .d..t...... signer/
2017/03/10 11:42:01 [10507] >f..t...... signer/keyconf.xml
2017/03/10 11:42:01 [10507] >f+++++++++ signer/sync.testfile
2017/03/10 11:42:01 [10505] sent 264 bytes  received 1,886 bytes  total size 65,346
```