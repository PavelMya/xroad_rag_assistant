### 3.26 UC SS\_25: Log In to a Hardware Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator logs in to a hardware token by
entering the PIN code of the token.

**Preconditions**:

-   The hardware token is initialized and connected to the system.

-   The token is in logged out state.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to make the functionality of the
token available to the system.

**Main Success Scenario**:

1.  SS administrator selects to log in to a hardware token.

2.  SS administrator enters the PIN code of the token.

3.  System parses the user input: 3.42.

4.  System verifies that the token is not locked.

5.  System verifies that the format of the entered PIN code is correct.

6.  System verifies that the PIN code is correct and logs in to the
    token.

7.  System logs the event “Log in to token” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error´message.
    - 3a.1. System displays the termination message from the parsing process.
    - 3a.2. System logs the event “Log in to token failed” to the audit log.
    - 3a.3. SS administrator selects to re-enter the PIN code. Use case continues form step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4-6a. The login attempt failed (e.g., token is inaccessible).
    - 4-6a.1. System displays the error message: ”Login failed: X”, where “X” is the error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 4-6a.2. System logs the event “Log in to token failed” to the auditlog.
    - 4-6a.3. SS administrator selects to re-enter the PIN code. Use casecontinues from step 3.
        - 4-6a.3a. SS administrator selects to terminate the use case.

- 4b. The security token is locked.
    - 4b.1. System displays the error message: “PIN locked”.
    - 4b.2. System logs the event “Log in to token failed” to the audit log.
    - 4b.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4b.3a. SS administrator selects to terminate the use case.

- 5b. The format of the entered PIN code is incorrect.
    - 5b.1. System displays the error message: “PIN format incorrect”.
    - 5b.2. System logs the event “Log in to token failed” to the audit log.
    - 5b.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 5b.3a. SS administrator selects to terminate the use case.

- 6b. The entered PIN code is incorrect.
    - 6b.1. System displays the error message: “Login failed: CKR\_PIN\_INCORRECT”.
    - 6b.2. System logs the event “Log in to token failed” to the audit log.
    - 6b.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 6b.3a. SS administrator selects to terminate the use case.

- 6c. The entered PIN code is incorrect and one login attempt is left.
    - 6c.1. System displays the error message: ”Login failed: CKR\_PIN\_INCORRECT, tries left: 1”.
    - 6c.2. System logs the event “Log in to token failed” to the audit log.
    - 6c.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 6c.3a. SS administrator selects to terminate the use case.

- 6d. The entered PIN code is incorrect and no login attempts are left.
    - 6d.1. System displays the error message: ”Login failed: CKR\_PIN\_INCORRECT. PIN locked.”.
    - 6d.2. System logs the event “Log in to token failed” to the audit log.
    - 6d.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 6d.3a. SS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.