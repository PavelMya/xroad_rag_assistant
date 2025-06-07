### 3.25 UC SS\_24: Log In to a Software Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator logs in to a software token by
entering the PIN code of the token.

**Preconditions**: The token is in logged out state.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to make the functionality of the
token available to the system.

**Main Success Scenario**:

1.  SS administrator selects to log in to a software token.

2.  SS administrator enters the PIN code of the token.

3.  System parses the user input: 3.42.

4.  System verifies that the PIN code is correct and logs in to the
    token.

5.  System logs the event “Log in to token” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the termination message from the parsing process.
    - 3a.2. System logs the event “Log in to token failed” to the audit log.
    - 3a.3. SS administrator selects to re-enter the PIN code. Use case continues form step 3.
    - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The entered PIN code is incorrect.
    - 4a.1. System displays the error message: “PIN incorrect”.
    - 4a.2. System logs the event “Log in to token failed” to the audit log.
    - 4a.3. SS administrator selects to re-enter the PIN code. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.