#### 3.5.3 Changing the Active Signing Key

Additional signing keys can be added with the following command:

```bash
confproxy-add-signing-key -p <PROXY_NAME> -t <SECURITY_TOKEN_ID>
```

Keys added in this manner will be marked as inactive keys ('signing-key-id-\*=&lt;KEY_ID&gt;') in the proxy instance configuration file (/etc/xroad/confproxy/&lt;PROXY_NAME&gt;/conf.ini). In case the current active signing key has to be replaced by one of the additional keys, the configuration file of the proxy instance will need to be modified, changing the following lines:

```ini
[configuration-proxy]
...
active-signing-key-id=QWERTY123
signing-key-id-1=QWERTY123
signing-key-id-2=321YTREWQ
```

to the following ones:

```ini
[configuration-proxy]
...
active-signing-key-id=321YTREWQ
signing-key-id-1=QWERTY123
signing-key-id-2=321YTREWQ
```

After the change the key 'QWERTY123' may be deleted if necessary.