#### 2.4.6 UC MEMBER\_49: Change a Security Server Client's Internal Server Connection Type

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator changes the connection type for a security server Member Owner or a security server client's internal servers that act as service clients.

**Preconditions**: -

**Postconditions**:

-   An audit log record is created for the event.

-   System accepts connections from the security server owner or client's internal servers that are of the type the SS administrator selected.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to change the internal server connection type for a security server owner or a security server client. By default the connection type for security server owner is set to HTTPS.

2.  SS administrator selects the connection type (HTTP, HTTPS, HTTPS NO AUTH).

3.  System saves the connection type.

4.  System logs the event “Set connection type for servers in service consumer role” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].