### 3.12 UC TRUST\_11: Delete an OCSP Responder of a CA

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator removes OCSP responder
information from a CA.

**Preconditions**: -

**Postconditions**:

-   An OCSP responder has been removed from a CA.

-   An audit log record for the event has been created.

**Trigger**: The information about an OCSP responder needs to be removed
from the configuration of an approved certification service.

**Main Success Scenario**:

1.  CS administrator selects to delete an OCSP responder of a CA.

2.  System deletes the OCSP responder information from the system
    configuration.

3.  System logs the event “Delete OCSP responder” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].