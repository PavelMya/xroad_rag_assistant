## 12. Configuration Backup and Restore

Access rights: System Administrator

The Central Server backs up
the database (excluding the database schema) and
the directories `/etc/xroad/` and `/etc/nginx/sites-enabled/`.

Backups contain sensitive information that must be kept secret (for example, private keys and database credentials). In other words, leaking this information could easily lead to full compromise of Central Server. Therefore, it is highly recommended that backup archives are encrypted and stored securely. Should the information still leak for whatever reason the Central Server should be considered as compromised and reinstalled from scratch.

Central Server backups are signed and optionally encrypted. The GNU Privacy Guard [GnuPG] is used for encryption and signing. Central Server's backup encryption key is generated during Central Server initialisation. In addition to the automatically generated backup encryption key, additional public keys can be used to encrypt backups.