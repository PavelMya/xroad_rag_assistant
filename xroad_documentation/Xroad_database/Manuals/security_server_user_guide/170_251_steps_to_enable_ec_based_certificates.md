### 25.1 Steps to Enable EC Based Certificates

Since version 7.6.0 Security Server supports ECDSA based authentication and signing keys. By default, both authentication and signing keys use the RSA algorithm as in previous versions. The EC algorithm can be enabled separately for authentication and/or signing keys so migration can be done in a gradual way. The instructions on how to start using EC based keys are listed below.

1. Update the configuration to use EC based keys. This can be done by updating the configuration file `/etc/xroad/conf.d/local.ini` and adding the following lines:

```ini
[proxy-ui-api]
authentication-key-algorithm = EC
signing-key-algorithm = EC
```

2. Restart the `xroad-proxy-ui-api` service to apply the changes made to the configuration file.
3. - Follow the instructions in Section [3.1](#31-configuring-the-signing-key-and-certificate-for-the-security-server-owner) to create new Signing certificate, which will be using EC algorithm now.
   - Follow the instructions in Section [3.2](#32-configuring-the-authentication-key-and-certificate-for-the-security-server) to create new Authentication certificate, which will be using EC algorithm now.