### 3.1.20 UC SERVICE\_18: Remove Access Rights from a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator removes subjects from the
access rights list of a service.

**Preconditions**: -

**Postconditions**:

-   One or more subjects have been removed from the access rights list
    of the service.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to remove subjects from the access
rights list of a service.

**Main** **Success** **Scenario**:

1.  SS administrator selects to remove subjects from the access rights
    list of a service.

2.  SS administrator selects the subjects to be removed.

3.  System deletes the access right records from the system
    configuration.

4.  System logs the event “Remove access rights from service” to the
    audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].