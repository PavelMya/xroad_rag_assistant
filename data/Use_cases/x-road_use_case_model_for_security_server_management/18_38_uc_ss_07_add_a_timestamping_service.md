### 3.8 UC SS\_07: Add a Timestamping Service

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator adds a timestamping service to
be used by the security server.

**Preconditions**: One or more timestamping services have been approved
by the X-Road governing agency.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to add a timestamping service to be
used by the security server to timestamp message log records.

**Main Success Scenario**:

1.  SS administrator selects to add a timestamping service.

2.  SS administrator selects the timestamping service that he wants to
    add to the security server from the list of approved timestamping
    services.

3.  System verifies that the selected timestamping service is not
    already configured to be used by the system.

4.  System saves the timestamping service to the list of timestamping
    services that can be used to timestamp message log records.

5.  System logs the event “Add timestamping service” to the audit log.

**Extensions**:

- 3a. SS administrator selected a timestamping service that already exists in the security server.
    - 3a.1. System displays an error message “Failed to add timestamping service: timestamping service already exists”.
    - 3a.2. System logs the event “Add timestamping service failed” to the audit log.
    - 3a.3. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].