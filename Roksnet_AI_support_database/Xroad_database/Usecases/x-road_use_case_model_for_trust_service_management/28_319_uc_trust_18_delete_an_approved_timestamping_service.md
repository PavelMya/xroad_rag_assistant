### 3.19 UC TRUST\_18: Delete an Approved Timestamping Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes an approved timestamping
service.

**Preconditions**: -

**Postconditions**: -

**Trigger**: An approved timestamping service needs to be removed from
the system configuration.

**Main Success Scenario**:

1.  CS administrator selects to delete an approved timestamping service.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System deletes the approved timestamping service information from
    the system configuration.

5.  System logs the event “Delete timestamping service” to the audit
    log.

**Extensions**:

- 3a. CS administrator selects not to delete the approved timestamping service and terminates the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].