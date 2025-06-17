#### 2.3.31 UC MEMBER\_33: Change the Management Service Provider

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator changes the management service provider.

**Preconditions**: The new management service provider (X-Road member's subsystem) must exist in the system configuration.

**Postconditions**:

-   The management service provider has been changed.

-   An audit log record for the event is created.

**Trigger**: The management service provider needs to be changed.

**Main Success Scenario**:

1.  CS administrator selects to change the management service provider.

2.  CS administrator selects the management service provider from the list of X-Road members' subsystems.

3.  System saves the changes.

4.  System logs the event “Edit provider of management services” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].