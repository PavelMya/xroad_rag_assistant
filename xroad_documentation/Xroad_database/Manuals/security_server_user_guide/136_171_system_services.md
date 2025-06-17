### 17.1 System Services

The most important system services of a Security Server are as follows.

| **Service**              | **Purpose**                                             | **Log**                                                                             |
|--------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------|
| `xroad-addon-messagelog` | Message log archiving and cleaning of the message logs  | `/var/log/xroad/messagelog-archiver.log`                                            |
| `xroad-confclient`       | Client process for the global configuration distributor | `/var/log/xroad/configuration_client.log`                                           |
| `xroad-proxy`            | Message exchanger                                       | `/var/log/xroad/proxy.log`                                                          |
| `xroad-signer`           | Manager process for key settings                        | `/var/log/xroad/signer.log`                                                         |
| `xroad-proxy-ui-api`     | Management UI and REST API                              | `/var/log/xroad/proxy_ui_api.log` and `/var/log/xroad/proxy_ui_api_access.log` |
| `xroad-monitor`          | Environmental monitoring                                | `/var/log/xroad/monitor.log`                                                        |
| `xroad-opmonitor`        | Operational monitoring                                  | `/var/log/xroad/op-monitor.log`                                                     |

System services are managed through the *systemd* facility.

**To start a service**, issue the following command as a `root` user:

    service  start

**To stop a service**, enter:

    service  stop

Services use the [default unit start rate limits](https://www.freedesktop.org/software/systemd/man/systemd-system.conf.html#DefaultStartLimitIntervalSec=).
An exception to this is `xroad-proxy-ui-api`, which uses a longer start rate limit ([5 starts / 40 seconds](https://github.com/nordic-institute/X-Road/blob/master/src/packages/src/xroad/ubuntu/generic/xroad-proxy-ui-api.service#L5-6))
to prevent infinite restart-loop in some specific error situations.

### 17.2 Logging configuration

For logging, the **Logback** system is used. Logback configuration files are stored in the directory `/etc/xroad/conf.d/`.

Default settings for logging are the following:

-   logging level: INFO;

-   rolling policy: whenever the file size reaches 100 MB.