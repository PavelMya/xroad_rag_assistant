#### 3.2.1 Configuration Structure of the Instances

Each global configuration that is to be mediated by the Configuration Proxy requires a proxy instance to be configured. The configuration of a proxy instance consists of a set of configuration files, including

* a trusted anchor .xml of the configuration being mediated;
* a configuration .ini file;
* verification certificates for the configured signing keys.

The following example file tree shows configured proxy instances named PROXY1 and PROXY2:

```bash
<configuration-path>/
|-PROXY1/
| |-cert_QWERTY123.pem
| |-cert_321YTREWQ.pem
| |-conf.ini
| \-anchor.xml
|-PROXY2/
| |-cert_1234567890.pem
| |-conf.ini
| \-anchor.xml
\-...
```

The configuration of proxy instances is described in [3.4](#34-proxy-instance-configuration).