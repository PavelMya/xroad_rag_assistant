### 3.15 UC TRUST\_14: Delete an Approved Certification Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes an approved
certification service.

**Preconditions**: -

**Postconditions**: -

**Trigger**: An approved certification service needs to be removed from
the system configuration.

**Main Success Scenario**:

1.  CS administrator selects to delete an approved certification
    service.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System deletes the approved certification service information from
    the system configuration.

5.  System logs the event “Delete certification service” to the audit
    log.

**Extensions**:

- 3a. CS administrator selects not to delete the approved certification service and terminates the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The certificates issued by the deleted certification service can no
    longer be used in the X-Road system.