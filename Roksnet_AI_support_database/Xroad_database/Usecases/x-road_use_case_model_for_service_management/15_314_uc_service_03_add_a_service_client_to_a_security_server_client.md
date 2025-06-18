#### 3.1.4 UC SERVICE\_03: Add a Service Client to a Security Server Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator grants access rights to a
security server client's services for a subject (a local access rights
group, a global access rights group or an X-Road member's subsystem).

**Preconditions**:

-   The subject has been registered in the central server (in case the
    subject is a global access rights group or an X-Road member's
    subsystem) or has been created in the security server (in case the
    subject is a local access rights group).

-   The security server client has one or more services.

-   The subject is not a service client of this security server client.

**Postconditions**:

-   The service client has been added to a security server client and
    access rights have been granted for the service client.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to grant access rights to a security
server client's services for a subject.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add a service client for a security
    server client.

2.  SS administrator selects the subject and the services to which to
    grant access rights. SS administrator can only add subsystems, local
    groups or global groups as a service client.

3.  System saves the access right records to the system configuration.

4.  System logs the event “Add access rights to subject” to the audit
    log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]