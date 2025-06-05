#### 11.1.7 Archive Encryption and Grouping

Archive files can be encrypted (when `archive-encryption-enabled = true`) using GnuPG ("gpg") which implements the OpenPGP (RFC 4880) specification. Please see e.g. [RFC 4880](https://www.ietf.org/rfc/rfc4880.txt) and [GnuPG](https://gnupg.org/) for more infomation. The encryption is enabled/disabled on a Security Server level - it's not possible to enable/disable it for specific subsystems only.

By default, the produced archive files contain messages from all the Security Server's members, but it's possible to group the archives by member or by subsystem if needed. The grouping is controlled by the setting `archive-grouping`. The grouping is enabled/disabled on a Security Server level - it is either enabled or disabled for all the members and subsystems.

Message log archive encryption and grouping can be configured separately. For example, the archives can be encrypted but not grouped (or vice versa). By default, both features are disabled.

When encryption is enabled, the archiving process expects to find a GnuPG keyring containing the server signing keypair in `archive-gpg-home-directory` (by default `/etc/xroad/gpghome`). When the default value is used the server signing keypair is the same as the backup signing and encryption keypair. This keypair is used to sign the generated archive files, and as a fallback encryption key if no other keys are configured.

The `archive-default-encryption-key` can be used to override the default encryption key id, which is used when `archive-grouping` is `none` or no member gpg key is defined. Changing this parameter requires restarting the xroad-addon-messagelog service.

In case `archive-grouping` is `member` or `subsystem`, gpg keys defined in file `archive-encryption-keys-config` are used (if no key is defined for the member, the default encryption key is used). This file maps member identifiers to gpg key identifiers and has the following format:
```