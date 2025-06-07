### 3.13 UC TRUST\_12: Add an Intermediate CA to a Certification Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator configures an intermediate CA
for a certification service.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Triggers**:

-   An intermediate CA needs to be described for the certification
    service.

-   Step 9 of 3.9.

**Main Success Scenario**:

1.  CS administrator selects to add an intermediate CA to a
    certification service.

2.  CS administrator selects and uploads the intermediate CA certificate
    file from the local file system.

3.  System verifies that the selected file is in DER or PEM format.

4.  System saves the selected certificate as the intermediate CA
    certificate and displays the message “Intermediate CA added
    successfully”.

5.  System logs the event “Add intermediate CA” to the audit log.

6.  CS administrator adds OCSP responders for the intermediate CA (if
    the OCSP responder information is not included in the intermediate
    CA certificate): 3.11.

**Extensions**:

- 3a. The selected file is not in DER or PEM format.
    - 3a.1. System displays the error message: “Failed to upload intermediate CA certificate: Incorrect file format. Only PEM and DER files allowed.”
    - 3a.2. System logs the event “Add intermediate CA failed” to the audit log.
    - 3a.2. CS administrator selects to reselect and upload the intermediate CA certificate. Use case continues from step 3.
        - 3a.2a. CS administrator selects to terminate the use case.

- 6a. CS administrator selects not to add OCSP responders to the intermediate CA (the OCSP responder information is included in the intermediate CA certificate) and terminates the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].