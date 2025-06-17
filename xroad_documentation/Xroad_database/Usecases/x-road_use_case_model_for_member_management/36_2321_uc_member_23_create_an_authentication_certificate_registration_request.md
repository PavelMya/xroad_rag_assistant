#### 2.3.21 UC MEMBER\_23: Create an Authentication Certificate Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates an authentication certificate registration request.

**Preconditions**: CS administrator is in possession of the information (the authentication certificate and the X-Road identifier of the security server) needed to create the request.

**Postconditions**: -

**Trigger**: The owner of the security server has forwarded a request for registering an authentication certificate for a security server to the X-Road governing authority.

**Main Success Scenario**:

1.  CS administrator selects to create an authentication certificate registration request.

2.  System displays the authentication certificate registration request, prefilling the known values.

3.  CS administrator uploads the authentication certificate file from the local file system and submits the request.

4.  System verifies that the uploaded file is in PEM or DER format and displays the message “Certificate imported successfully”.

5.  System verifies that no other authentication certificate registration request have been created in the central server for this authentication certificate. The previously created requests that are in the *revoked* or *declined* state are not included in this verification.

6.  System saves the authentication certification registration request and sets the status of the request: [2.3.10](#2310-uc-member_13-set-registration-request-status).

7.  System displays the message “Request of adding authentication certificate to existing security server 'X' added successfully”, where “X” is the X-Road identifier of the security server.

8.  System logs the event “Add authentication certificate for security server” to the audit log.

**Extensions**:

3a. CS administrator decides not to create the request and terminates the use case.

4a. The uploaded file is not in PEM or DER format.

  - 4a.1. System displays the error message: “Failed to import authentication certificate: Incorrect file format. Only PEM and DER files allowed.”.

  - 4a.2. CS administrator selects to re-upload the authentication certificate. Use case continues from step 4.

    - 4a.2a. CS administrator selects to terminate the use case.

5a. The authentication certificate is already registered or submitted for registration with another authentication certificate registration request.

  - 5a.1. System displays the error message “Failed to add authentication certificate adding request: Certificate is already submitted for registration with request 'X'”, where “X” is the identifier of the registration request that contains the certificate.

  - 5a.2. System logs the event “Add authentication certificate for security server failed” to the audit log.

  - 5a.3 CS administrator selects to re-upload the authentication certificate. Use case continues from step 4.

    - 5a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].