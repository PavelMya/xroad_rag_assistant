### 21.1 Steps to Enable EC Based Signing Keys

Since version 7.6.0 Central Server supports ECDSA based configuration signing keys. By default, both internal and external configuration signing keys use the RSA algorithm as in previous versions. The EC algorithm can be enabled separately for internal and external keys so migration can be done in steps, e.g., first internal and then external keys or vice versa. The instructions on how to start using internal and external signing EC keys are listed below.

1. Update the configuration to use EC based keys. This can be done by updating the configuration file `/etc/xroad/conf.d/local.ini` and adding the following lines:

```ini
[admin-service]
internal-key-algorithm = EC
external-key-algorithm = EC
```

2. Restart the `xroad-center` service to apply the changes made to the configuration file.
3. Follow the instructions in the [Generating a Configuration Signing Key](#541-generating-a-configuration-signing-key) to generate new keys, which will be using EC algorithm now.