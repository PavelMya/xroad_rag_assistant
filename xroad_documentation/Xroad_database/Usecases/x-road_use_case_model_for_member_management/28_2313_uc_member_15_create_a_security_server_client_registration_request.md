#### 2.3.13 UC MEMBER\_15: Create a Security Server Client Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates a security server client registration request for registering an X-Road member's subsystem as a client of a security server.

**Preconditions**: CS administrator is in possession of the information (the X-Road identifier of the client to be registered and the X-Road identifier of the security server) needed to register an X-Road member's subsystem as a client of a security server.

**Postconditions**: -

**Trigger**: The X-Road member has forwarded a request for registering as a security server client to the X-Road governing authority.

**Main Success Scenario**:

1.  CS administrator selects to create a security server client registration request for an X-Road member's subsystem.

2.  System displays the security server client registration request, prefilling the known values.

3.  CS administrator inserts the information needed to create the registration request – the X-Road identifiers of the client and the security server (unless prefilled by the system) and submits the request.

4.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

5.  System verifies that the client is not already registered as a client of the security server.

6.  System verifies that no other security server client registration request containing the submitted information have been created in the central server. The previously created requests that are in the *revoked* or *declined* state are not included in this verification.

7.  System saves the security server client registration request and sets the status of the request: [2.3.10](#2310-uc-member_13-set-registration-request-status).

8.  System verifies that the subsystem inserted to the registration request as the client does not already exists for the X-Road member and saves the subsystem information to the system configuration.

9.  System displays the message “Request of adding client 'X' to security server 'Y' added successfully”, where “X” is the X-Road identifier of the security server.

10. System logs the event “Register member as security server client” to the audit log.

**Extensions**:

3a. CS administrator selects not to submit the request and terminates the use case.

4a. The parsing of the user input terminated with an error message.

  - 4a.1. System displays the error message “Failed to add new server client request: X”, where “X” is the termination message of the parsing process.

  - 4a.2. System logs the event “Register member as security server client failed” to the audit log.

  - 4a.3 CS administrator selects to reinsert the information. Use case continues from step 4.

    - 4a.3a. CS administrator selects to terminate the use case.

5a. The inserted client is already registered as a client of the security server.

  -  5a.1. System displays the error message: Failed to add new server client request: 'X' has already been registered as a client to security server 'Y'”, where “X” is the X-Road identifier of the client and “Y” is the X-Road identifier of the security server.

  - 5a.2. System logs the event “Register member as security server client failed” to the audit log.

  - 5a.3. CS administrator selects to reinsert the information needed to create the registration request. Use case continues from step 4.

    - 5a.3a. CS administrator selects to terminate the use case.

6a. A request for registering the client to the security server has already been created.

  - 6a.1. System displays the error message: “Failed to add new server client request: A request for registering 'X', as a client to security server 'Y' has already been submitted (Z, request ID: 'ZZ')'”, where

    -   “X” is the X-Road identifier of the client,

    -   “Y” is the X-Road identifier of the security server,

    -   “Z” is the date and time of when the existing request was saved to the system configuration and

    -   “ZZ” is the identifier of the existing request.

  - 6a.2. System logs the event “Register member as security server client failed” to the audit log.

  - 6a.3. CS administrator selects to reinsert the information needed to create the registration request. Use case continues from step 4.

    - 6a.3a. CS administrator selects to terminate the use case.

8a. A subsystem code was not inserted or a subsystem with the inserted code already exists for this X-Road member.

- 8a.1. The use case continues from step 8.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].