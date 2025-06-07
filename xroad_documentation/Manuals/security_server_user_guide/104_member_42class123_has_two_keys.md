## Member #42/CLASS/#123 has two keys:
   \#42/CLASS/\#123 = ABCD....
   \#42/CLASS/\#123 = EF12....
```
* There can be several mappings (keys) per member (one mapping per line)
* Lines _starting with_ `#` are ignored
* Escaping special characters in the _member identifier_ part:
  * `=` is written as `\=` (a literal `\=` becomes `\\=`)
  * `#` is written as `\#` (a literal `\#` becomes `\\#`)

Warning. The archiving process fails if a required key is not present in the gpg keyring. Therefore, it is important to verify that the mappings are correct.

**Configuration example**

Generate a keypair for encryption with defaults and no expiration and export the public key:
```bash
gpg [--homedir ] --quick-generate-key INSTANCE/memberClass/memberCode default default never
gpg [--homedir ] --export INSTANCE/memberClass/memberCode >INSTANCE-memberClass-memberCode.pgp
```

Import the public key to the gpg keyring in `archive-gpg-home-directory` and take note of the key id.
```bash
gpg --homedir  --import INSTANCE-memberClass-memberCode.pgp
```

Edit the key and add ultimate trust.
```bash
gpg --homedir  --edit-key 
```

At the `gpg>` prompt, type `trust`, then type `5` for ultimate trust, then `y` to confirm, then `quit`.

Add the mapping to `archive-encryption-keys-config` file (mappings can be edited without restarting X-Road services), e.g.:
```bash
INSTANCE/memberClass/memberCode = 96F20FF6578A5EF90DFBA18D8C003019508B5637
```

Add the mapping file location (`archive-encryption-keys-config`) and grouping level (`archive-grouping`) to `/etc/xroad/conf.d/local.ini` file (editing the file requires restarting X-Road services), e.g.:
```bash
[message-log]
archive-encryption-enabled = true
archive-grouping = member
archive-encryption-keys-config = /etc/xroad/messagelog/archive-encryption-mapping.ini
```

To decrypt the encrypted archives, use the following syntax:
```bash
gpg [--homedir ] --decrypt  --output 
```