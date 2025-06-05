#### 2.2.8 UC GCONF\_08: Log In to a Hardware Security Token

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator logs in to a hardware token by
entering the token PIN code.

**Preconditions**:

-   The hardware security token is initialized and connected to the
    system.

-   The token is in logged out state.

**Postconditions**: An audit log record for the event has been created.

**Triggers**:

-   CS administrator wishes to make the functionality of the token
    available to the system.

-   Step 4a.1. of 2.2.11.

**Main Success Scenario**:

1.  CS administrator selects log in to a hardware security token holding
    a configuration signing key.

2.  CS administrator enters the token PIN code.

3.  System parses the user input: 2.2.16.

4.  System verifies, that the token is not locked.

5.  System verifies that the entered PIN code conforms to the PIN code
    format configured for the token.

6.  System verifies the entered PIN code is correct and logs in to the
    token.

7.  System logs the event “Log in to token” to the audit log.

**Extensions**:

- 3a. The parsing of the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Log in to token failed” to the audit log.
    - 3a.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

- 4-6a. The login attempt failed (e.g., incorrect PIN was entered).
    - 4-6a.1. System displays the error message: “Login failed: X”, where “X” is the error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 4-6a.2. System logs the event “Log in to token failed” to the audit log.
    - 4-6a.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4-6a.3a. CS administrator selects to terminate the use case.

- 4b. The token is inaccessible.
    - 4b.1. System displays the error message: “Token 'X' not available”, where “X” is the identifier of the security token.
    - 4b.2. System logs the event “Log in to token failed” to the audit log.
    - 4-6a.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4-6a.3a. CS administrator selects to terminate the use case.

- 4b. The security token is locked (too many incorrect PIN entries).
    - 4b.1. System displays the error message: “PIN locked”.
    - 4b.2. System logs the event “Log in to token failed” to the audit log.
    - 4b.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4b.3a. CS administrator selects to terminate the use case.

- 5b. The format of the entered PIN code is not acceptable for the token.
    - 5b.1. System displays the error message: “PIN format incorrect”.
    - 5b.2. System logs the event “Log in to token failed” to the audit log.
    - 5b.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 5b.3a. CS administrator selects to terminate the use case.

- 6b. The entered PIN code is incorrect and one login attempt is left.
    - 6b.1. System displays the error message: “Login failed: CKR\_PIN\_INCORRECT, tries left: 1”.
    - 6b.2. System logs the event “Log in to token failed” to the audit log.
    - 6b.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 6b.3a. CS administrator selects to terminate the use case.

- 6c. The entered PIN code is incorrect and no login attempts are left (i.e., the token is locked).
    - 6c.1. System displays the error message: “Login failed: CKR\_PIN\_INCORRECT. PIN locked.”.
    - 6c.2. System logs the event “Log in to token failed” to the audit log.
    - 6c.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 6b.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].