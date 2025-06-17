### 12.7 Verifying Backup Archive Consistency

During restore Central Server verifies consistency of backup archives automatically, archives are not checked during upload.
Also, it is possible to verify the consistency of the archives externally. For verifying the consistency externally,
Central Server's public key is needed. When backups are encrypted, then a private key for decrypting archive is also needed.
GPG uses "sign then encrypt" scheme, so it is not possible to verify encrypted archives without decrypting them.

Automatic backup verification is only possible when original Central Server keypair is available. Should keypair on the
Central Server be lost for whatever reason, automatic verification is no longer possible. Therefore, it is recommended
to export backup encryption public key and import it into separate secure environment. If backups are encrypted,
Central Server public key should be imported to keyrings holding additional encryption keys, so that backups can be
decrypted and verified in these separate environments.

To export Central Servers backup encryption public key use the following command:

    gpg --homedir /etc/xroad/gpghome --armor --output server-public-key.gpg --export 

where `` is the Central Server instance id,
for example, `EE`.

Resulting file (`server-public-key.gpg`) should then be exported from Central Server and imported to GPG keystore used
for backup archive consistency verification.