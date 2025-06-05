### 13.4 Backup Encryption Configuration

Backups are always signed, but backup encryption is initially turned off. To turn encryption on, please override the
default configuration in the file `/etc/xroad/conf.d/local.ini`, in the `[proxy]` section (add or edit this section).

```ini
[proxy]

backup-encryption-enabled = true
backup-encryption-keyids = <keyid1>, <keyid2>, ...
```

To turn backup encryption on, change the `backup-encryption-enabled` property to true. Additional
encryption keys can be imported in the `/etc/xroad/gpghome` keyring and key identifiers listed using the `backup-encryption-keyids` parameter. It is recommended to set up at least one additional key, otherwise the backups will be unusable in case Security Servers private key is lost. It is up to Security Servers administrator to check that keys used are sufficiently strong, there are no automatic checks.

Warning. All keys listed in `backup-encryption-keyids` must be present in the gpg keyring or backup fails.

Additional keys for backup encryption should be generated and stored outside Security Server in a secure environment.
After gpg keypair has been generated, public key can be exported to a file (backupadmin@example.org is the name of the
key being exported) using this command:

    gpg --output backupadmin.publickey --armor --export backupadmin@example.org

Resulting file `backupadmin.publickey` should be moved to Security Server and imported to backup gpg keyring. Administrator should make sure that the key has not been changed during transfer, for example by validating the key fingerprint.

Private keys corresponding to additional backup encryption public keys must be handled safely and kept in secret. Any of
them can be used to decrypt backups and thus mount attacks on the Security Servers.

**Configuration example**

Generate a keypair for encryption with defaults and no expiration and export the public key:
```bash
gpg [--homedir <admin gpghome>] --quick-generate-key backupadmin@example.org default default never
gpg [--homedir <admin gpghome>] --export backupadmin@example.org >backupadmin@example.org.pgp
```

Import the public key to the gpg keyring in `/etc/xroad/gpghome` directory and take note of the key id.
```bash
gpg --homedir /etc/xroad/gpghome --import backupadmin@example.org.pgp
```

Edit the key and add ultimate trust.
```bash
gpg --homedir /etc/xroad/gpghome/ --edit-key <key id>
```

At the `gpg>` prompt, type `trust`, then type `5` for ultimate trust, then `y` to confirm, then `quit`.

Add the key id to `/etc/xroad/conf.d/local.ini` file (editing the file requires restarting X-Road services), e.g.:
```bash
[proxy]
backup-encryption-enabled = true
backup-encryption-keyids = 96F20FF6578A5EF90DFBA18D8C003019508B5637
```

To decrypt the encrypted backups, use the following syntax:

```bash
gpg --homedir /etc/xroad/gpghome --decrypt <backup name> --output <output file name>
```