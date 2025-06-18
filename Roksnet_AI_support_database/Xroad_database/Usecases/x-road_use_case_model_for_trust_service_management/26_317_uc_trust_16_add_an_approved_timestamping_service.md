### 3.17 UC TRUST\_16: Add an Approved Timestamping Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator adds a timestamping service to
the list of approved timestamping services.

**Preconditions**:

-   The timestamping service has been approved by the X-Road governing
    agency.

-   CS administrator has received the information from the timestamping
    service provider that is needed to configure the timestamping
    service in the central server.

**Postconditions**: -

**Trigger**: A timestamping service is approved by the X-Road governing
agency for providing timestamping services to X‑Road members.

**Main Success Scenario**:

1.  CS administrator selects to add an approved timestamping service.

2.  CS administrator inserts the URL of the timestamping server.

3.  CS administrator selects and uploads the TSA certificate file from
    the local file system.

4.  System verifies that the uploaded file is in DER or PEM format and
    displays the message “Certificate imported successfully”.

5.  System parses the user input: 3.20.

6.  System verifies that the inserted URL is in correct format.

7.  System verifies, that an approved timestamping service with the
    inserted URL and certificate does not already exist in the system
    configuration.

8.  System saves the timestamping service information.

9.  System logs the event “Add timestamping service” to the audit log.

**Extensions**:

- 4a. The uploaded file is not in DER or PEM format.
    - 4a.1. System displays the error message: “Failed to upload approved TSA certificate: Incorrect file format. Only PEM and DER files allowed.”.
    - 4a.2. CS administrator selects to reselect and upload the certificate file. Use case continues from step 4.
        - 4a.2a. CS administrator selects to terminate the use case.

- 5a. The parsing of the user input terminated with an error message.
    - 5a.1. System displays the termination message of the parsing process.
    - 5a.2. System logs the event “Add timestamping service failed” to the audit log.
    - 5a.3. CS administrator selects to reinsert the URL. Use case continues  from step 5.
        - 5a.3a. CS administrator selects to terminate the use case.

- 6a. The URL is malformed.
    - 6a.1. System displays the error message: “Timestamping server URL 'X' is an invalid URL, examples of valid URL-s: 'http://www.example.com', 'https://www.example.com'”, where “X” is the inserted URL.
    - 6a.2. System logs the event “Add timestamping service failed” to the audit log.
    - 6a.3. CS administrator selects to reinsert the URL. Use case continues from step 5.
        - 6a.3a. CS administrator selects to terminate the use case.

- 7a. An approved timestamping service with the inserted URL and certificate already exists.
    - 7a.1. System displays the error message “An approved timestamping service with the inserted URL and certificate already exists”.
    - 7a.2. System logs the event “Add timestamping service failed” to the audit log.
    - 7a.3. CS administrator selects to reinsert the URL. Use case continues from step 5.
        - 7a.3a. CS administrator selects to reselect and upload the certificate file. Use case continues from step 4.
        - 7a.3b. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].