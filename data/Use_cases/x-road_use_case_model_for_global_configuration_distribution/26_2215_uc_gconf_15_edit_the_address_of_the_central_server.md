#### 2.2.15 UC GCONF\_15: Edit the Address of the Central Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator changes the address of the
central server.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Trigger**: CS administrator wishes to change the address on which the
central server is available for incoming requests (e.g., management
service requests, configuration download requests).

**Main Success Scenario**:

1.  CS administrator selects to change the public address of the central
    server.

2.  CS administrator inserts the address.

3.  System parses the user input 2.2.16.

4.  System verifies, that the inserted address is a valid DNS name or IP
    address.

5.  System saves the address.

6.  System logs the event “Edit central server address” to the audit
    log.

7.  System generates configuration anchors for the internal and external
    configuration: 2.2.17.

**Extensions**:

- 3a. The parsing of the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Edit central server address failed” to the audit log.
    - 3a.3. User selects to reinsert the address. Use case continues from step 3.
        - 3a.3a. User selects to terminate the use case.

- 4a. The inserted address is not valid.
    - 4a.1. System displays the error message: “Central server address must be DNS name or IP address”.
    - 4a.2. System logs the event “Edit central server address failed” to the audit log.
    - 4a.3. User selects to reinsert the address. Use case continues from step 3.
        - 4a.3a. User selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].