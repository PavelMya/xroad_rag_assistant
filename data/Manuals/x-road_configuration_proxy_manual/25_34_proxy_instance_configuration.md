### 3.4 Proxy Instance Configuration

1)  Create configuration files for the new proxy instance by invoking the 'confproxy-create-instance -p &lt;PROXY_NAME&gt;' command. Afterwards, use the 'confproxy-view-conf -p &lt;PROXY_NAME&gt;' command to verify that the operation has been successfully completed (example output follows):

```bash
confproxy-create-instance -p PROXY

Populating 'conf.ini' with default values.
Done.

confproxy-view-conf -p PROXY

Configuration for proxy 'PROXY'
Validity interval: 600 s.
anchor.xml
================================================
'anchor.xml' could not be loaded: IOError: /etc/xroad/confproxy/PROXY/anchor.xml (No such file or directory)
Configuration URLs
================================================
http://1.2.3.4/PROXY/conf
https://1.2.3.4/PROXY/conf
Signing keys and certificates
================================================
active-signing-key-id:
    NOT CONFIGURED (add 'active-signing-key-id' to 'conf.ini')
```

2) Generate a signing key and a self signed certificate for the newly created proxy instance using the following command:

```bash
confproxy-add-signing-key -p <PROXY_NAME> -t <SECURITY_TOKEN_ID> [-a <RSA|EC>]
```

Note: **-a** parameter is optional and can be used to specify the key algorithm(since version 7.6.0). If not provided, the default value is RSA. If keys are using EC algorithm and consumers of the Configuration Proxy are using older X-Road instances then they will fail to verify global configuration signatures.

If no active signing key is configured for the proxy instance, then the new key should be set as the currently active key (example output follows):

```bash
confproxy-add-signing-key -p PROXY -t 0

Generated key with ID QWERTY123
No active key configured, setting new key as active in conf.ini
Saved self-signed certificate to cert_QWERTY123.pem
confproxy-view-conf -p PROXY
...
Signing keys and certificates
================================================
active-signing-key-id:
QWERTY123 (Certificate: /etc/xroad/confproxy/PROXY/cert_QWERTY123.pem)
```
Alternatively, one may add an existing key using the '–k &lt;KEY_ID&gt;' argument:

```bash
confproxy-add-signing-key -p PROXY -k QWERTY123

No active key configured, setting new key as active in conf.ini
Saved self-signed certificate to cert_QWERTY123.pem
```

3) To define which global configuration this proxy instance should distribute, download the source anchor from an X-Road Central Server and save it as '/etc/xroad/confproxy/&lt;PROXY_NAME&gt;/anchor.xml'.

4) The Configuration Proxy should be operational at this point. The periodic cron job (once a minute) should download the global configuration defined in '/etc/xroad/confproxy/&lt;PROXY_NAME&gt;/anchor.xml' and generate a directory for distribution. The output of 'confproxy-view-conf -p &lt;PROXY_NAME&gt;' should be similar to the following:

```bash
confproxy-view-conf -p PROXY

Configuration for proxy 'PROXY'
Validity interval: 600 s.
anchor.xml
================================================
Instance identifier: AA
Generated at: UTC 2014-11-17 09:28:56
Hash: 3A:3D:B2:A4:D3:FC:E8:08:7E:EA:8A:92:5C:6E:92:0C:70:C8
Configuration URLs
================================================
http://1.2.3.4/PROXY/conf
https://1.2.3.4/PROXY/conf
Signing keys and certificates
================================================
active-signing-key-id:
QWERTY123 (Certificate: /etc/xroad/confproxy/PROXY/cert_QWERTY123.pem)
```

5) To let clients download the generated global configuration an anchor file needs to be generated using the following command:

```bash
confproxy-generate-anchor -p <PROXY_NAME> -f <ANCHOR_FILENAME>
```

If generation was successful the output should be simply:

```bash
confproxy-generate-anchor -p PROXY -f /home/xroad/anchor.xml

Generated anchor xml to '/home/xroad/anchor.xml'
```

6) To make sure that the global configuration is being distributed correctly use the '/usr/share/xroad/scripts/download_instance_configuration.sh' script, giving it &lt;ANCHOR_FILENAME&gt; and the path, which should hold the downloaded files, as arguments (example output follows):

```bash
mkdir test_download
/usr/share/xroad/scripts/download_instance_configuration.sh anchor.xml test_download/

... - Downloading configuration from http://1.2.3.4/PROXY/conf
... - Downloading content from http://1.2.3.4/PROXY/123/AA/shared-params.xml
... - Saving SHARED-PARAMETERS to test_download/AA/shared-params.xml
... - Saving content to file test_download/AA/shared-params.xml
... - Downloading content from http://1.2.3.4/PROXY/123/AA/private-params.xml
... - Saving PRIVATE-PARAMETERS to test_download/AA/private-params.xml
... - Saving content to file test_download/AA/private-params.xml
```
If the proxy instance has been configured correctly, the 'test_download' directory should contain the downloaded global configuration files.