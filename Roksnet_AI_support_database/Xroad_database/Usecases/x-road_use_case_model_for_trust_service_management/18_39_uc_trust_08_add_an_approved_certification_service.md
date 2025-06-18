### 3.9 UC TRUST\_08: Add an Approved Certification Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator adds a certification service to
the list of approved certification services.

**Preconditions**:

-   The certification service has been approved by the X-Road governing
    agency.

-   CS administrator has received the certificates and OCSP responder
    information from the certification service provider that are needed
    to configure the certification service in the central server.

-   A Java class that describes the certificate profile for the
    certification service has been developed.

**Postconditions**: -

**Trigger**: A certification service is approved by the X-Road governing
agency for providing certification services to X-Road members.

**Main Success Scenario**:

1.  CS administrator selects to add an approved certification service.

2.  CS administrator selects and uploads the certification service CA
    certificate file from the local file system.

3.  System verifies that the uploaded file is in DER or PEM format.

4.  System displays the message “Certificate imported successfully” and
    prompts for certification service settings.

5.  CS administrator

    a.  selects whether the certificates issued by the certification
        service can be used only for authentication or also for signing;

    b.  inserts the fully qualified name of the Java class that
        describes the certificate profile for the certification service.

6.  System parses the user input: 3.20.

7.  System verifies, that the Java class that describes the certificate
    profile exists in the system's classpath and saves the changes.

8.  System saves the selected certificate as the certification service
    CA certificate and the settings inserted for the service and
    displays the message “Certification service added successfully”.

9.  System logs the event “Add certification service” to the audit log.

10. CS administrator adds OCSP responders for the certification service
    CA (if the OCSP responder information is not included in the
    certification service CA certificate): 3.11.

11. CS administrator adds intermediate CAs for the certification
    service: 3.13.

**Extensions**:

- 3a. The uploaded file is not in DER or PEM format.
    - 3a.1. System displays the error message: “Failed to upload service CA certificate: Incorrect file format. Only PEM and DER files allowed.”
    - 3a.2. CS administrator selects to reselect and upload the certification service CA certificate. Use case continues from step 3.
        - 3a.2a. CS administrator selects to terminate the use case.

- 5a. CS administrator selects not to edit the certification service settings and terminates the use case.

- 6a. The parsing of the user input terminated with an error message.
    - 6a.1. System displays the termination message of the parsing process.
    - 6a.2. System logs the event “Add certification service failed” to the audit log.
    - 6a.3. CS administrator selects to reinsert the certificate profile class name. Use case continues from step 6.
        - 6a.3a. CS administrator selects to terminate the use case.

- 7a. System did not find the inserted certificate profile class on the classpath.
    - 7a.1. System displays the error message “Certificate profile with name 'X' does not exist.”, where “X” is the inserted class name.
    - 7a.2. System logs the event “Add certification service failed” to the audit log.
    - 7a.3. CS administrator selects to reinsert the certificate profile class name. Use case continues from step 6.
        - 7a.3a. CS administrator selects to terminate the use case.

- 10a. CS administrator selects not to add OCSP responders to the certification service CA (the OCSP responder information is included in the certification service CA certificate).
    - 10a.1. CS administrator terminates the use case.
        - 10a.1a. CS administrator selects to add intermediate CAs for the certification service. Use case continues from step 11.

- 11a. CS administrator selects not to add intermediate CAs for the certification service and terminates the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].