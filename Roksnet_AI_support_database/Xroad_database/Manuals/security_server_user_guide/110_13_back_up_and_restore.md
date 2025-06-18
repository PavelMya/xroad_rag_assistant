## 13 Back up and restore

It is possible to back up and later restore Security Server configuration. A backup archive file contains the
following configuration:

- copy of serverconf database
- user modifiable configuration files
- keys and certificates
  - Security Server's auth key and certificate
  - members' sign keys and certificates (that are stored in soft token)
  - Security Server's internal TLS key and certificate
  - Security Server's UI key and certificate
- database credentials

Notice that starting from X-Road v7.0, the backup archive file no longer contains the local override file `/etc/xroad/services/local.conf`, but instead `/etc/xroad/services/local.properties` file will be included.

**N.B.** Message log database encryption keys, and message log archives encryption and signing keys are included in the backups only if they are stored under the `/etc/xroad` directory. However, they should not be stored in the `/etc/xroad/gpghome` subdirectory since it is excluded from the backups.

Backups contain sensitive information that must be kept secret (for example, private keys and database credentials).
In other words, leaking this information could easily lead to full compromise of Security Server. Therefore, it is
highly recommended that backup archives are encrypted and stored securely. Should the information still leak for whatever
reason the Security Server should be considered as compromised and reinstalled from scratch.

Security server backups are signed and optionally encrypted. The GNU Privacy Guard [GnuPG] is used for encryption and signing.
Security server's backup encryption key is generated during Security Server initialisation. In addition to the
automatically generated backup encryption key, additional public keys can be used to encrypt backups.