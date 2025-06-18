### 6.1 The configuration file

The file `/etc/xroad/services/local.properties` replaces the file `/etc/xroad/services/local.conf` starting from X-Road version 7.

The `local.properties` file's contents consists of key-value pairs such as `XROAD_SIGNER_PARAMS=-XX:MaxMetaspaceSize=100m`. Notice that you cannot use quotes in the values. If you have multiple values for one key, use space to separate the values e.g. `XROAD_SIGNER_PARAMS=-Xmx100m -XX:MaxMetaspaceSize=100m`. Also notice that with `local.properties` you can only add new parameters and override old ones – you cannot remove existing default parameters.

Example of `/etc/xroad/services/local.properties` with modifications that override the default Java memory parameters for Security Server:

```properties
XROAD_PROXY_PARAMS=-Xms200m -Xmx1024m
```

Example of `/etc/xroad/services/local.properties` with modifications that override the default Java memory parameters for Central Server:

```properties
XROAD_CS_ADMIN_SERVICE_PARAMS=-Xms200m -Xmx1024m
```

Example of `/etc/xroad/services/local.properties` with modifications that override the default Spring Boot parameter for Central Servers management API:

```properties
XROAD_CS_ADMIN_SERVICE_PARAMS=-Dserver.forward-headers-strategy=NONE
```

All possible properties to adjust in this file:

| Property                             | Details                                              |
|--------------------------------------|------------------------------------------------------|
| XROAD_PARAMS                         | Parameters for all processes                         |
| XROAD_SIGNER_PARAMS                  | Parameters for the Signer                            |
| XROAD_ADDON_PARAMS                   | Parameters for all addons                            |
| XROAD_CONFCLIENT_PARAMS              | Parameters for the Configuration Client              |
| XROAD_CONFPROXY_PARAMS               | Parameters for the Configuration Proxy               |
| XROAD_MESSAGELOG_ARCHIVER_PARAMS     | Parameters for the Message Log Archiver              |
| XROAD_MONITOR_PARAMS                 | Parameters for the Environmental Monitor             |
| XROAD_OPMON_PARAMS                   | Parameters for the Operational Monitor               |
| XROAD_PROXY_PARAMS                   | Parameters for the Security Server                   |
| XROAD_PROXY_UI_API_PARAMS            | Parameters for the Security Server's admin API       |
| XROAD_SIGNER_CONSOLE_PARAMS          | Parameters for the Signer Console                    |
| XROAD_CS_ADMIN_SERVICE_PARAMS        | Parameters for the Central Server's admin API        |
| XROAD_CS_REGISTRATION_SERVICE_PARAMS | Parameters for the Central Server's registration API |
| XROAD_CS_MANAGEMENT_SERVICE_PARAMS   | Parameters for the Central Server's management API   |