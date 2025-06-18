### 13.2 Archiving the Audit Log

In order to save hard disk space and avoid loss of the audit log records during Central Server crash, it is recommended to archive the audit log files periodically to an external storage or a log server.

The X-Road software does not offer special tools for archiving the audit log. The rsyslog can be configured to redirect the audit log to an external location.