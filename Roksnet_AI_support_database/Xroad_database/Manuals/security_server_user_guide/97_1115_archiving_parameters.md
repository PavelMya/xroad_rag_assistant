#### 11.1.5 Archiving Parameters

1. `keep-records-for` – time in days for which to keep timestamped and archived records in the database. Defaults to `30`.
2. `archive-max-filesize` – maximum size for archived files in bytes. Reaching the maximum value triggers the file rotation. Defaults to `33554432` (32 MB).
3. `archive-interval` – time interval as Cron expression \[[CRON](#Ref_CRON)\] for archiving timestamped records. Defaults to `0 0 0/6 1/1 * ? *` (fire every 6 hours).
4. `archive-path` – the directory where the timestamped log records are archived. Defaults to `/var/lib/xroad/`.
5. `clean-interval` – time interval as Cron expression \[[CRON](#Ref_CRON)\] for cleaning archived records from the database. Defaults to `0 0 0/12 1/1 * ? *` (fire every 12 hours).
6. `archive-transfer-command` – the command executed after the (periodic) archiving process. This enables one to configure an external script to transfer archive files automatically from the Security Server. Defaults to no operation.
7. `archive-grouping` - archive file grouping; `none` (default), by `member` or, by `subsystem`.
8.  `archive-encryption-enabled` - archive file encryption enabled: false (default) or true.
9.  `archive-gpg-home-directory` - GPG home directory for archive file signing and encryption keyring (default `/etc/xroad/gpghome`).
10. `archive-encryption-keys-config` - Configuration file for member gpg keys.
11. `archive-default-encryption-key` - Default archive encryption key id.