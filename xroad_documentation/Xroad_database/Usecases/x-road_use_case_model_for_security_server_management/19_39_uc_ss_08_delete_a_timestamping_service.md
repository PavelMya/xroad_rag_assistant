### 3.9 UC SS\_08: Delete a Timestamping Service

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator deletes a timestamping service
from the security server.

**Preconditions**: -

**Postconditions**:

-   The security server can no longer use the deleted timestamping
    service to timestamp message log records.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to delete a timestamping service.

**Main Success Scenario**:

1.  SS administrator selects to delete a timestamping service.

2.  System deletes the selected timestamping service from the list of
    usable timestamping services.

3.  System logs the event “Delete timestamping service” to the audit
    log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].