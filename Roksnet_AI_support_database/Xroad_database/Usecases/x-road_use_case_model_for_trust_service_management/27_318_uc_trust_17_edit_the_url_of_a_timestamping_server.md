### 3.18 UC TRUST\_17: Edit the URL of a Timestamping Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator edits the URL of a timestamping
server.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Trigger**: The URL on which the timestamping service is being provided
has changed.

**Main Success Scenario**:

1.  CS administrator selects to edit the URL of a timestamping server.

2.  CS administrator inserts the URL.

3.  System parses the user input: 3.20.

4.  System verifies that the inserted URL is in correct format.

5.  System saves the timestamping URL, replacing the previous value.

6.  System logs the event “Edit timestamping service” to the audit log.

**Extensions**:

- 3a. The parsing of the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Edit timestamping service failed” to the audit log.
    - 3a.3. CS administrator selects to reinsert the URL. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

- 4a. The URL is malformed.
    - 4a.1. System displays the error message: “Timestamping server URL 'X' is an invalid URL, examples of valid URL-s: 'http://www.example.com', 'https://www.example.com'”, where “X” is the inserted URL.
    - 4a.2. System logs the event “Edit timestamping service failed” to the audit log.
    - 4a.3. CS administrator selects to reinsert the URL. Use case continues from step 3.
        - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].