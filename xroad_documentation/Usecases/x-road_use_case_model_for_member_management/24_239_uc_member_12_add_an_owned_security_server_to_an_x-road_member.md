#### 2.3.9 UC MEMBER\_12: Add an Owned Security Server to an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates an authentication certificate registration request.

**Preconditions**: CS administrator is in possession of the information (authentication certificate and security server code) needed to register the security server for the X-Road member.

**Postconditions**: -

**Trigger**: The owner of the security server has forwarded a request for registering a security server to the X-Road governing authority. The request must include the authentication certificate and the code of the security server.

**Main Success Scenario**:

1.  CS administrator selects to add an owned security server to an X-Road member.

2.  System displays the authentication certificate registration request, prefilling the known values.

3.  CS administrator inserts the security server code.

4.  CS administrator uploads the authentication certificate file from the local file system.

5.  CS administrator submits the request.

6.  System verifies that the uploaded file is in PEM or DER format and is an authentication certificate (certificate is an authentication certificate, if it has *ExtendedKeyUsage* extension which contains *ClientAuthentication* or if it has *keyUsage* extension which has *digitalSignature*, *keyEncipherment* or *dataEncipherment* bit set); and displays the message “Certificate imported successfully”.

7.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

8.  System verifies that no other authentication certificate registration request have been created in the central server for this authentication certificate. The previously created requests that are in the *revoked* or *declined* state are not included in this verification.

9.  System verifies that a security server with the entered code is not already registered as an owned server for the X-Road member.

10. System saves the authentication certification registration request and sets the status of the request: [2.3.10](#2310-uc-member_13-set-registration-request-status).

11. System displays the message “Request of adding authentication certificate to new security server 'X' added successfully”, where “X” is the X-Road identifier of the security server.

12. System logs the event “Add security server” to the audit log.

**Extensions**:

5a. CS administrator decides not to submit the request and terminates the use case.

6a. The uploaded file is not in PEM or DER format.

  - 6a.1. System displays the error message: “Failed to import authentication certificate: Incorrect file format. Only PEM and DER files allowed.”.

  - 6a.2. CS administrator selects to re-upload the authentication certificate. Use case continues from step 5.

    - 6a.2a. CS administrator selects to terminate the use case.

6b. The uploaded certificate is not an authentication certificate.

  - 6b.1. System displays the error message: “Failed to import authentication certificate: This certificate cannot be used for authentication.”.

  - 6b.2. CS administrator selects to re-upload the authentication certificate. Use case continues from step 5.

    - 6b.2a. CS administrator selects to terminate the use case.

7a. The parsing of the user input terminated with an error message.

  - 7a.1. System displays the error message “Failed to add new owned server request: X”, where “X” is the termination message of the parsing process.

  - 7a.2. System logs the event “Add security server failed” to the audit log.

  - 7a.3 CS administrator selects to reinsert the server code. Use case continues from step 5.

    - 7a.3a. CS administrator selects to terminate the use case.

8a. The authentication certificate is already registered or submitted for registration with another authentication certificate registration request.

  - 8a.1. System displays the error message “Failed to add new owned server request: Certificate is already submitted for registration with request 'X'”, where “X” is the identifier of the registration request that contains the certificate.

  - 8a.2. System logs the event “Add security server failed” to the audit log.

  - 8a.3 CS administrator selects to re-upload the authentication certificate. Use case continues from step 5.

    - 8a.3a. CS administrator selects to terminate the use case.

9a. A security server with the submitted code is already registered as an owned server for the X-Road member

  - 9a.1. System displays the error message “Failed to add new owned server request: Server with owner class 'X', owner code 'Y' and server code 'Z' already exists.”, where “X” is the member class and “Y” the member code of the X-Road member the security server is being added to and “Z” is the inserted server code.

  - 9a.2. System logs the event “Add security server failed” to the audit log.

  - 9a.3 CS administrator selects to reinsert the server code. Use case continues from step 5.

    - 9a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].