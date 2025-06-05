# PostgreSQL 10 & 12 (RHEL 7, 8; Ubuntu 20.04)
wal_level = replica

max_wal_senders   = 3   # should be ~ number of secondaries plus some small number. Here, we assume there are two secondaries.
wal_keep_segments = 8   # keep some wal segments so that secondaries that are offline can catch up.