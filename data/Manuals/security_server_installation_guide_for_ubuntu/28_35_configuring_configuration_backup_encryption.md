### 3.5 Configuring Configuration Backup Encryption

It is possible to automatically encrypt Security Server configuration backups. Security Server uses The GNU Privacy Guard (https://www.gnupg.org)
for backup encryption and verification. Backups are always signed, but backup encryption is initially turned off.
To turn encryption on, please override the default configuration in the file `/etc/xroad/conf.d/local.ini`, in the `[proxy]` section (add or edit this section).

    [proxy]
    backup-encryption-enabled = true
    backup-encryption-keyids = <keyid1>, <keyid2>, ...

To turn backup encryption on, please change the `backup-encryption-enabled` property value to `true`.
By default, backups are encrypted using Security Server's backup encryption key. Additional encryption keys can be imported in the /etc/xroad/gpghome keyring and key identifiers listed using the backup-encryption-keyids parameter. It is recommended to set up at least one additional key, otherwise the backups will be unusable in case Security Server's private key is lost. It is up to Security Server's administrator to check that keys used are sufficiently strong, there are no automatic checks.

Warning. All keys listed in backup-encryption-keyids must be present in the gpg keyring or backup fails.

All these keys are used to encrypt backups so that ANY of these keys can decrypt the backups. This is useful both for verifying encrypted backups'
consistency and decrypting backups in case Security Server's backup encryption key gets lost for whatever reason.

To externally verify a backup archive's consistency, Security Server's backup encryption public key has to be exported
and imported into external GPG keyring. Note that this can be done only after Security Server has been initialised - the
Security Server backup encryption key is generated during initialisation.

To export Security Server's backup encryption public key use the following command:

    gpg --homedir /etc/xroad/gpghome --armor --output server-public-key.gpg --export AA/GOV/TS1OWNER/TS1

where `AA/GOV/TS1OWNER/TS1` is the Security Server id.

The key can then be moved to an external host and imported to GPG keyring with the following command:

    gpg --homedir /your_gpg_homedir_here --import server-public-key.gpg