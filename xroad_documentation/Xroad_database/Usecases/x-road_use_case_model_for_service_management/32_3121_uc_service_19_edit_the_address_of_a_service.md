#### 3.1.21 UC SERVICE\_19: Edit the Address of a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the address of a
service.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to change the address of a service.

**Main** **Success** **Scenario**:

1.  SS administrator selects to edit the address of a service.

2.  SS administrator inserts the address.

3.  System parses the user input: 3.1.13.

4.  System verifies that the inserted URL is valid.

5.  System verifies that the protocol part of the URL of the service is
    “https” and sets the value for TLS certification verification to
    “true”.

6.  System saves the service address to the system configuration.

7.  System logs the event “Edit service parameters” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the termination message from the parsing process.
    - 3a.2. System logs the event “Edit service parameters failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the URL. Use case continues from step 3.
    - 3a.3a. SS administrator selects to terminate the use case.

- 4a. SS administrator inserted an invalid URL.
    - 4a.1. System displays the error message “Invalid URL format, must begin with 'http' or 'https'”.
    - 4a.2. System logs the event “Edit service parameters failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the URL. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. The protocol part of the URL is “http”.
    - 5a.1. Use case continues from step 6.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].