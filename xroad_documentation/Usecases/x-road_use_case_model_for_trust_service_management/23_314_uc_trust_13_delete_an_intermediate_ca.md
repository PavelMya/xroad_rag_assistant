### 3.14 UC TRUST\_13: Delete an Intermediate CA

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes an intermediate CA from
a certification service.

**Preconditions**: -

**Postconditions**:

-   The information about an intermediate CA has been deleted.

-   An audit log record for the event has been created.

**Trigger**: An intermediate CA needs to be removed from a certification
service.

**Main Success Scenario**:

1.  CS administrator selects to delete an intermediate CA from a
    certification service.

2.  System deletes the intermediate CA information from the system
    configuration.

3.  System logs the event “Delete intermediate CA” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].