### 13.2 Restore from the Command Line

To restore configuration from the command line, the following data must be available:

-   The X-Road ID of the Security Server

To find the X-Road ID of the Security Server, the following command can be used:

    cat /etc/xroad/gpghome/openpgp-revocs.d/.rev | grep uid

It is expected that the restore command is run by the xroad user.

In order to restore configuration, the following command should be used:

    /usr/share/xroad/scripts/restore_xroad_proxy_configuration.sh \
    -s  -f  [-P -N]

For example (all on one line):

    /usr/share/xroad/scripts/restore_xroad_proxy_configuration.sh \
    -s AA/GOV/TS1OWNER/TS1 \
    –f /var/lib/xroad/backup/conf_backup_20140703-110438.gpg

In case original backup encryption and signing key is lost additional parameters can be specified to skip decryption and/or
signature verification. Use `-P` command line switch when backup archive is already decrypted externally and `-N` switch to
skip checking archive signature.

If a backup is restored on a new uninitialized (the initial configuration hasn't been completed) Security Server, the
Security Server's gpg key must be manually created before restoring the backup:

    /usr/share/xroad/scripts/generate_gpg_keypair.sh /etc/xroad/gpghome 

If it is absolutely necessary to restore the system from a backup made on a different Security Server, the forced mode
of the restore command can be used with the –F option together with unencrypted backup archive flags. For example (all on one line):

    /usr/share/xroad/scripts/restore_xroad_proxy_configuration.sh \
    -F -P –f /var/lib/xroad/backup/conf_backup_20140703-110438.tar

In case backup archives were encrypted they have to be first unencrypted in external safe environment and then securely
transported to Security Server filesystem.