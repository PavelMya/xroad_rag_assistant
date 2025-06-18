### 6.8 Configuring a Minimum Required Client Security Server Version

Service providers can configure a minimum required X-Road software version for client Security Servers. It means that client Security Servers older than the configured version cannot access the services.

Service providers can configure the required minimum version in the `/etc/xroad/conf.d/local.ini` configuration file using the `proxy.server-min-supported-client-version` system property. For example:

```
[proxy]
server-min-supported-client-version=7.0.0
```

The property has no value by default, meaning a minimum version hasn't been set. Instead, when the value is set, all the minor and patch versions starting from the configured version are approved.