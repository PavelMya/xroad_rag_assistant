### 3.11 UC TRUST\_10: Add or Edit an OCSP Responder of a CA

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator describes an OCSP responder
service information for a CA.

**Preconditions**: CS administrator has received the OCSP responder
information (URL and/or certificate) from the certification service
provider.

**Postconditions**: -

**Triggers**:

-   An OCSP responder needs to be described for a CA.

-   Step 8 of 3.9.

-   Step 6 of 3.13.

**Main Success Scenario**:

1.  CS administrator selects to add or edit an OCSP responder of a CA.

2.  CS administrator inserts the URL of the OCSP server.

3.  CS administrator selects and uploads the certificate file used by
    the OCSP server to sign OCSP responses from the local file system.

4.  System verifies that the uploaded file is in DER or PEM format.

5.  System parses the user input: 3.20.

6.  System verifies that the inserted URL is in correct format.

7.  System saves the OCSP responder information.

8.  System logs the event “Add OCSP responder of certification service”
    or “Edit OCSP responder”, depending on whether the OCSP responder
    was added or edited, to the audit log.

**Extensions**:

- 3a. CS administrator selects not to upload a certificate for the OCSP responder. Use case continues from step 5.

- 4a. The uploaded file is not in DER or PEM format.
    - 4a.1. System displays the error message: “Failed to upload OCSP responder certificate: Incorrect file format. Only PEM and DER files allowed.”.
    - 4a.2. CS administrator selects to reselect and upload the certificate file. Use case continues from step 4.
        - 4a.2a. CS administrator selects to terminate the use case.

- 5a. The parsing of the user input terminated with an error message.
    - 5a.1. System displays the termination message of the parsing process.
    - 5a.2. System logs the event “Add OCSP responder of certification service failed” or “Edit OCSP responder failed”, depending on whether the OCSP responder was added or edited, to the audit log.
    - 5a.3. CS administrator selects to reinsert the URL. Use case continues from step 3.
        - 5a.3a. CS administrator selects to terminate the use case.

- 6a. The URL is malformed.
    - 6a.1. System displays the error message: “'X' is an invalid URL, examples of valid URL-s: 'http://www.example.com', 'https://www.example.com' ”, where “X” is the inserted URL.
    - 6a.2. System logs the event “Add OCSP responder of certification service failed” or “Edit OCSP responder failed”, depending on whether the OCSP responder was added or edited, to the audit log.
    - 6a.3. CS administrator selects to reinsert the URL. Use case continues from step 3.
        - 6a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].