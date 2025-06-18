### 3.23 UC SS\_22: Edit the Friendly Name of a Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator changes the friendly name of a
security token.

**Preconditions**: The token information is saved in the system
configuration.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to change the friendly name of a
security token.

**Main Success Scenario**:

1.  SS administrator selects to change the friendly name of a security
    token and changes the name.

2.  System parses the user input: 3.42.

3.  System saves the changes to the system configuration.

4.  System logs the event “Set friendly name to token” to the audit log.

**Extensions**:

- 2a. The process of parsing the user input terminated with an error message.
    - 2a.1. System displays the termination message from the parsing process.
    - 2a.2. System logs the event “Set friendly name to token failed” to the audit log.
    - 2a.3. SS administrator selects to reinsert the friendly name. Use case continues form step 2.
        - 2a.3a. User selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.