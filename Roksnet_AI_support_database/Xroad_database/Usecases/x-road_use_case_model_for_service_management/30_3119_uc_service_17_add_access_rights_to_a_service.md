#### 3.1.19 UC SERVICE\_17: Add Access Rights to a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the access rights to
a security server client's service by adding subjects to the access
rights list. Only X-Road member's subsystems, local groups or global
groups can be added to the access rights list.

**Preconditions**: The subjects are not in the access rights list of
this service.

**Postconditions**:

-   The subjects have been added to the access rights list of the
    security server client's service.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to change access rights for a
security server client's service.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add subjects to the access rights list
    of a service.

2.  SS administrator selects the subjects to add to the access rights
    list. Only an X-Road member's subsystem, a local group or a global
    group can be added to the access rights list.

3.  System saves the access right records to the system configuration.

4.  System logs the event “Add access rights to service” to the audit
    log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].