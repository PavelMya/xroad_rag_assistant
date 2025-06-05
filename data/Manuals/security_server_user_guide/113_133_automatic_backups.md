### 13.3 Automatic Backups

By default the Security Server backs up its configuration automatically once every day. Backups older than 30 days are
automatically removed from the server. If needed, backup removal policies can be adjusted by editing the
`/etc/cron.d/xroad-proxy` file.

Automatic backup schedule can be adjusted  in the file `/etc/xroad/conf.d/local.ini`,
in the `[configuration-client]` section (add or edit this section).

```ini
[configuration-client]
proxy-configuration-backup-cron=0 15 3 * * ?
```

**Note:** In cases where automatic backup is not required (ex: extensions which rely on configuration-client)
it is suggested to disable it by using cron expression that will never trigger. For example `* * * * * ? 2099`