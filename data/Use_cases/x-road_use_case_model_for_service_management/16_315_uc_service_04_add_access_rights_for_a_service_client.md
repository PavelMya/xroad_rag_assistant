#### 3.1.5 UC SERVICE\_04: Add Access Rights for a Service Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator adds access rights for a
service client.

**Preconditions**: The security server client has one or more services
whose access rights have not been granted for the service client.

**Postconditions**:

-   The access rights to one or more services have been added for the
    service client.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to add access rights for a service
client.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add access rights for a service client.

2.  SS administrator selects the services to which to grant access
    rights for. SS administrator can only select the services to which
    the service client does not already have access rights for.

3.  System saves the access right records to the system configuration.

4.  System logs the event “Add access rights to subject” to the audit
    log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]