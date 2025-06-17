## 21 Adding command line arguments

If you need to add command line arguments for the Security Server, for example if you wish to increase Java's maximum heap size, you can do it with the properties file `/etc/xroad/services/local.properties`. The file is also included in the backup archive file when taking a backup of the Security Server's configuration.

Example of `/etc/xroad/services/local.properties` with modifications that override the default Java memory parameters:

```properties
XROAD_PROXY_PARAMS=-Xms150m -Xmx1024m
```

All possible properties to adjust in this file are:
```
XROAD_SIGNER_PARAMS
XROAD_ADDON_PARAMS
XROAD_CONFCLIENT_PARAMS
XROAD_CONFPROXY_PARAMS
XROAD_JETTY_PARAMS
XROAD_MESSAGELOG_ARCHIVER_PARAMS
XROAD_MONITOR_PARAMS
XROAD_OPMON_PARAMS
XROAD_PROXY_PARAMS
XROAD_PROXY_UI_API_PARAMS
XROAD_SIGNER_CONSOLE_PARAMS
```