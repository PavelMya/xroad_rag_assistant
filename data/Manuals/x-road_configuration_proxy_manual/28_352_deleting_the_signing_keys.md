#### 3.5.2 Deleting the Signing Keys

Should a signing key need to be deleted, the following command can be used:

```bash
confproxy-del-signing-key -p <PROXY_NAME> -k <SIGNING_KEY_ID>
```

where &lt;SIGNING_KEY_ID&gt; can be found in the output of 'confproxy-view-conf' (example output follows):

```bash
confproxy-del-signing-key -p PROXY -k QWERTY123

Deleted key from signer
Deleted key from conf.ini
Deleted self-signed certificate 'cert_QWERTY123.pem'
```

Attempts to delete the active signing key will be unsuccessful.