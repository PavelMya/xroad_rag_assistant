### 12.3 Restoring the Configuration from the Command Line

To restore configuration from the command line, the following data must be available:
- the instance ID of the Central Server and,
- in HA setup, the node name of the Central Server.

It is expected that the restore command is run by the xroad user.

Use the following command to restore configuration in non-HA setup:
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -i  -f  [-P -N]
```

In HA setup, this command has an additional mandatory parameter, the node name:
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -i  -n  -f  [-P -N]
```

For example (all in one line, non-HA setup):
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -i EE -f /var/lib/xroad/backup/conf_backup_20230515-114736.gpg
```

For example (all in one line, HA setup):
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -i EE -n node_0 -f /var/lib/xroad/backup/conf_backup_20230515-114736.gpg
```

In case original backup encryption and signing key is lost additional parameters can be specified to skip decryption and/or signature verification. Use `-P` command line switch when backup archive is already decrypted externally and `-N` switch to skip checking archive signature.

If a backup is restored on a new uninitialized (the initial configuration hasn't been completed) Central Server, the Central Server's gpg key must be manually created before restoring the backup:
```bash
/usr/share/xroad/scripts/generate_gpg_keypair.sh /etc/xroad/gpghome 
```

If it is absolutely necessary to restore the system from a backup made on a different Central Server, the forced mode of the restore command can be used with the –F option. For example:
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -F -P -f /var/lib/xroad/backup/conf_backup_20230515-114736.tar
```

In case backup archives were encrypted they have to be first unencrypted in external safe environment and then securely transported to Central Server filesystem.

It is possible to restore the configuration while skipping the database restoration by appending the -S switch, e.g.
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -i  -f  -S
```

To see all the possible parameters use the -h switch, e.g.
```bash
/usr/share/xroad/scripts/restore_xroad_center_configuration.sh -h
```