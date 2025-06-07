### 3.4 Backup Encryption Configuration

It is possible to automatically encrypt Central Server configuration backups. Central Server uses The GNU Privacy Guard (https://www.gnupg.org)
for backup encryption and verification. Backups are always signed, but backup encryption is initially turned off.
To turn encryption on, please override the default configuration in the file `/etc/xroad/conf.d/local.ini`, in the `[center]` section (add or edit this section).
```bash
[center]

backup-encryption-enabled = true
backup-encryption-keyids = , , ...
```

To turn backup encryption on, please change the `backup-encryption-enabled` property value to `true`.
By default, backups are encrypted using Central Server's backup encryption key. Additional encryption keys can be imported in the `/etc/xroad/gpghome` keyring and key identifiers listed using the `backup-encryption-keyids` parameter. It is recommended to set up at least one additional key, otherwise the backups will be unusable in case Central Server's private key is lost. It is up to Central Server's administrator to check that keys used are sufficiently strong, there are no automatic checks.

Warning. All keys listed in `backup-encryption-keyids` must be present in the gpg keyring or backup fails.

All these keys are used to encrypt backups so that ANY of these keys can decrypt the backups. This is useful both for verifying encrypted backups'
consistency and decrypting backups in case Central Server's backup encryption key gets lost for whatever reason.

To externally verify a backup archive's consistency, Central Server's backup encryption public key has to be exported
and imported into external GPG keyring. Note that this can be done only after Central Server has been initialised - the
Central Server backup encryption key is generated during initialisation.

To export Central Server's backup encryption public key use the following command:
```bash
gpg --homedir /etc/xroad/gpghome --armor --output server-public-key.gpg --export EE
```
where `EE` is the Central Server instance identifier.

The key can then be moved to an external host and imported to GPG keyring with the following command:
```bash
gpg --homedir  --import server-public-key.gpg
```

## 4 Additional configuration

### 4.1 Global configuration V1 support

The support for global configuration version V1 has been removed in X-Road version 6.20.

### 4.2 Global configuration V2 support

The Central Server produces global configuration version V2. Version V2 is supported by Security Servers from version 6.8.0 and up.

### 4.3 Global configuration V3 support

The Central Server produces global configuration version V3. Version V3 is supported by Security Servers from version 7.4.0 and up.