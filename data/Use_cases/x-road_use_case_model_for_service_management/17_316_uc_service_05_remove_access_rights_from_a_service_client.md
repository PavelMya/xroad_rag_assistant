#### 3.1.6 UC SERVICE\_05: Remove Access Rights from a Service Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator removes access rights form a
service client.

**Preconditions**: -

**Postconditions**:

-   Access rights to one or more services have been removed from the
    service client.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to remove access rights form a
service client.

**Main** **Success** **Scenario**:

1.  SS administrator selects to remove service access rights from a
    service client.

2.  SS administrator selects the services to which to remove the access
    rights.

3.  System deletes the access right records from the system
    configuration.

4.  System logs the event “Remove access rights from subject” to the
    audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].