#### 7.2.1 Pausing the database and configuration synchronization

1. Pause the database synchronization. Assuming that the `serverconf` database is running in port `5433`, issue the
    following command:

    ```bash
    # PostgreSQL version < 10
    sudo -u postgres psql -p 5433 -c 'select pg_xlog_replay_pause();'
    ```

    ```bash
    # PostgreSQL version >= 10
    sudo -u postgres psql -p 5433 -c 'select pg_wal_replay_pause();'
    ```

2. Disable the configuration synchronization on the secondary nodes:
    ```bash
    sudo -u xroad touch /var/tmp/xroad/sync-disabled
    ```
    **Note:** Check that the synchronization service is configured to honor the `sync-disabled` flag. See the chapter on
    [Setting up periodic configuration synchronization on the secondary nodes](#52-set-up-periodic-configuration-synchronization-on-the-secondary-nodes)
    for more details.