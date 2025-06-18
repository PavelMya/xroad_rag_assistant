#### 11.1.3 Message Log Encryption

The message bodies can be encrypted (`messagelog-encryption-enabled = true`) when stored to the database. By default, the encryption is disabled. Also, the encryption is fully transparent to all the external interfaces, e.g., the signed document download service. The encryption is symmetric, the used cipher is AES-CTR, and the encryption is performed using Java code.

In the message log database, there are two separate columns for plaintext (`message`) and encrypted (`ciphermessage`) message body. The message body is always stored in one of the two columns depending on the configuration. Instead, the other column that is not used is left empty. When message log database encryption is enabled/disabled, the change doesn't affect already existing records in the database. For example, when message log database encryption is enabled, all the records created after the configuration change will be encrypted and stored in the `ciphermessage` column. Instead, all the records stored before the change will remain in plaintext in the `message` column.

When encryption is switched on, the implementation expects to find the keystore in the location pointed by `messagelog-keystore`. The keystore should contain an encryption key with the identifier/alias specified in `messagelog-key-id`. The keystore password is specified in `messagelog-keystore-password`.

For example, add the following to `/etc/xroad/conf.d/local.ini`:

```ini
[message-log]
messagelog-encryption-enabled=true
messagelog-keystore=/etc/xroad/messagelog/messagelog.p12
messagelog-keystore-password=somepassword
messagelog-key-id=key1
```

Create the password store and import a key:

```bash
keytool -keystore /etc/xroad/messagelog/messagelog.p12 -storetype pkcs12 -importpassword -alias key1
```

Finally, restart `xroad-proxy` service.

To view the encrypted messages at some later stage, use the ASIC web service documented in \[[UG-SIGDOC](#Ref_UG-SIGDOC)\]. The web service performs automatic decryption, where needed.