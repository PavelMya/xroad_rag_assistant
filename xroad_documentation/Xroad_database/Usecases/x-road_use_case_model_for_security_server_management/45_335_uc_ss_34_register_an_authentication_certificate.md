### 3.35 UC SS\_34: Register an Authentication Certificate

**System**: Security server

**Level**: User task

**Component:** Security server, central server

**Actors**: SS administrator, central server

**Brief Description**: SS administrator sends an authentication
certificate registration request to the central server.

**Preconditions**: The certificate is in “saved” state.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to register an authentication
certificate for the security server.

**Main Success Scenario**:

1.  SS administrator selects to register an unregistered authentication
    certificate.

2.  System prompts for DNS name/IP address of the security server.

3.  SS administrator inserts the DNS name or IP address of the security
    server.

4.  System parses the user input: 3.42.

5.  System verifies that the DNS name or IP address is valid.

6.  System creates the registration request, finds the management
    service address from the global configuration and sends the request
    to the central server. The contents of the request is described in
    \[[PR-MSERV](#Ref_PR-MSERV)\].

7.  System receives the response message from central server and
    verifies that the response is not an error message.

8.  System displays the message “Request sent” to the SS administrator
    and sets the registration state of the certificate to “registration
    in progress”.

9.  System logs the event “Register authentication certificate” to the
    audit log.

**Extensions**:

- 4a. The process of parsing the user input terminated with an error message.
    - 4a.1. System displays the termination message from the parsing process.
    - 4a.2. System logs the event “Register authentication certificate failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert DNS name or IP address. Use case continues form step 2.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. The DNS name or IP address is not valid.
    - 5a.1. System displays the error message “Failed to register certificate: Invalid host address”.
    - 5a.2. System logs the event “Register authentication certificate failed” to the audit log.
    - 5a.3. SS administrator selects to reinsert the DNS name or IP address. Use case continues form step 2.
        - 5a.3a. SS administrator selects to terminate the use case.

- 6a. Creating or sending the error message failed.
    - 6a.1. System displays the error message “Failed to register certificate: X”, where “X” is the error message.
    - 6a.2. System logs the event “Register authentication certificate failed” to the audit log.
    - 6a.3. Use case terminates.

- 7a. Central server responded with an error message.
    - 7a.1. System displays the error message “Failed to register certificate: X”, where “X” is the error message received from the central server.
    - 7a.2. System logs the event “Register authentication certificate failed” to the audit log.
    - 7a.3. Use case terminates.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.