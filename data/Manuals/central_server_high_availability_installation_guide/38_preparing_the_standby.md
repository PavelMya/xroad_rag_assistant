### Preparing the standby

* Verify that the standby PostgreSQL instance is not running.
* Clear the data directory (on Ubuntu, default location is `/var/lib/postgresql/<version>/<cluster name>`)

  ```bash
   rm -rf /path/to/data/directory/*
  ```

* Do a base backup with `pg_basebackup`:
  
  ```bash
  sudo -u postgres pg_basebackup -h <master> -U standby --slot=standby_node1 -R -D /path/to/data/directory/
  ```


* Additional settings:
  * Postgresql version < 12: Edit `recovery.conf` (in the data directory) and verify the settings:
  
  ```properties
  standby_mode = 'on'
  primary_conninfo = 'host=<master> user=<standby> password=<password>'
  primary_slot_name = 'standby_node1'
  recovery_target_timeline = 'latest'
  ```
   * Postgresql version >=12: Previous settings were moved to `postgresql.conf` instead and standby_mode is not used anymore. A standby.signal file in the data directory is used instead. (https://www.postgresql.org/docs/current/recovery-config.html):
  ```properties
  primary_conninfo = 'host=<master> user=<standby> password=<password>'
  primary_slot_name = 'standby_node1'
  recovery_target_timeline = 'latest'
  ```
  
  Where `<master>` is the DNS or IP address of the master node and `<standby>` and `<password>` are the credentials of the replication user (see https://www.postgresql.org/docs/current/runtime-config-replication.html#RUNTIME-CONFIG-REPLICATION-STANDBY).

* Start the standby server.