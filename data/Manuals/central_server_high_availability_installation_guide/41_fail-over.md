### Fail-over

In case the master server fails, one can manually promote the standby to a master by executing the following command on the standby server:
```bash
sudo pg_ctl promote
```

On Ubuntu pg_ctl is typically not in the path, use pg_ctlcluster instead:
```bash
sudo pg_ctlcluster <major version> <cluster name> promote