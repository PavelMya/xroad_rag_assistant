#### 2.2.7 UC GCONF\_07: Log In to a Software Security Token

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator logs in to a software token by
entering the token PIN code.

**Preconditions**: The token is in logged out state.

**Postconditions**: An audit log record for the event has been created.

**Triggers**:

-   CS administrator wishes to make the functionality of the token
    available to the system.

-   Step 4a.1. of 2.2.11.

**Main Success Scenario**:

1.  CS administrator selects log in to a software security token.

2.  CS administrator enters the token PIN code.

3.  System parses the user input: 2.2.16.

4.  System verifies the PIN code is correct and logs in to the token.

5.  System logs the event “Log in to token” to the audit log.

**Extensions**:

- 3a. The parsing of the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Log in to token failed” to the audit log.
    - 3a.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

- 4a. The entered PIN code is incorrect:
    - 4a.1. System displays the error message: “PIN incorrect”.
    - 4a.2. System logs the event “Log in to token failed” to the audit log.
    - 4a.3. CS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_PR-GCONF)\].