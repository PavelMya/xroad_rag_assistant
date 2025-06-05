### 12.1 Changing the Configuration of the Audit Log

The X-Road software writes the audit log to the *syslog* (*rsyslog*) using UDP interface (default port is 514). Corresponding configuration is located in the file

    /etc/rsyslog.d/90-udp.conf

The audit log records are written with level INFO and facility LOCAL0. By default, log records of that level and facility are saved to the X-Road audit log file

    /var/log/xroad/audit.log

The default behavior can be changed by editing the *rsyslog* configuration file

    /etc/rsyslog.d/40-xroad.conf

Restart the *rsyslog* service to apply the changes made to the configuration file

    service rsyslog restart

The audit log is rotated monthly by *logrotate*. To configure the audit log rotation, edit the *logrotate* configuration file

    /etc/logrotate.d/xroad-proxy