#### 2.4.7 UC MEMBER\_50: Add a Security Server Client's Internal TLS Certificate

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator uploads an internal TLS certificate for a security server Member Owner or a security server client.

**Preconditions**: -

**Postconditions**: An audit log record is created for the event.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to add an internal TLS certificate for a security server Member Owner or a security server client.

2.  SS administrator selects and uploads a certificate file from the local file system.

3.  System verifies that the uploaded file is in PEM or DER format.

4.  System verifies that this certificate is not already saved in the system configuration for this security server client.

5.  System saves the certificate and displays the message: “Certificate imported successfully”.

6.  System logs the event “Add internal TLS certificate” to the audit log.

**Extensions**:

3a. The uploaded file is not in PEM or DER format.

  - 3a.1. System displays the error message: “Incorrect file format. Only PEM and DER files allowed.”.

  - 3a.2. System logs the event “Add internal TLS certificate failed” to the audit log.

  - 3a.3. SS administrator selects to re-upload the certificate. Use case continues from step 3.

    - 3a.3a. SS administrator selects to terminate the use case.

4a. The uploaded certificate has already been saved for the security server client.

  - 4a.1. System displays the error message: “Certificate already exists”.

  - 4a.2. System logs the event “Add internal TLS certificate failed” to the audit log.

  - 4a.3. SS administrator selects to re-upload the certificate. Use case continues from step 3.

    - 4a.3a. SS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].