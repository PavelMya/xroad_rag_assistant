### Verifying replication

On master, check pg_stat_replication view:
```bash
sudo -iu postgres psql -txc "SELECT * FROM pg_stat_replication"
...
username         | standby
...
state            | streaming
sent_lsn         | 0/2A03F000
write_lsn        | 0/2A03F000
flush_lsn        | 0/2A03F000
replay_lsn       | 0/2A03F000
```

On stanbys, check pg_stat_wal_receiver view:
```bash
sudo -iu postgres psql -txc "SELECT * FROM pg_stat_wal_receiver"
...
status                | streaming
receive_start_lsn     | 0/29000000
received_lsn          | 0/2A03F000
last_msg_send_time    | 2019-12-30 07:32:03.902888+00
last_msg_receipt_time | 2019-12-30 07:32:03.903118+00
...
slot_name             | standby_node1
```

The `status` should be _streaming_ and `sent_lsn` on master should be close to `received_lsn` on the stanbys. If replication slots are in use, one can also compare the `sent_lsn` and `replay_lsn` values on the master.