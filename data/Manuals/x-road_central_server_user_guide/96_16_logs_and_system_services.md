## 16. Logs and System Services

Most significant Central Server services are the following:

| Service                           | Purpose                                                |                                                     Log |
|-----------------------------------|--------------------------------------------------------|--------------------------------------------------------:|
| xroad-center                      | X-Road Central Server admin UI and REST management API |        `/var/log/xroad/centralserver-admin-service.log` |
| xroad-center-registration-service | X-Road Central Server Registration Service             | `/var/log/xroad/centralserver-registration-service.log` |
| xroad-center-management-service   | X-Road Central Server Management Service               |   `/var/log/xroad/centralserver-management-service.log` |
| xroad-signer                      | The service that manages key settings                  |                             `/var/log/xroad/signer.log` |
| nginx                             | The Web server that distributes global configuration   |                                       `/var/log/nginx/` |

System services can be managed using the systemd facility.
To start a service, issue the following command as a root user:

`systemctl start <service>`

To stop a service, enter:

`systemctl stop <service>`

To read logs, a user must have root user's rights or belong to the xroad system group.

For logging, the Logback system is used.

Logback configuration files are stored in the `/etc/xroad/conf.d/` directory.

Default settings for logging are the following:
- logging level: INFO;
- rolling policy: whenever file size reaches 100 MB.