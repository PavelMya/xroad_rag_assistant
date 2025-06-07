#### 3.1.27 UC SERVICE\_25: Add a Local Group for a Security Server Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator adds a local group to a
security server client.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to add a local group to a security
server client.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add a local group to a security server
    client.

2.  SS administrator inserts the code and description for the local
    group.

3.  System parses the user input: 3.1.13.

4.  System verifies that a local group with the inserted code does not
    already exist for this security server client in the system
    configuration.

5.  System saves the information about the local group to the system
    configuration.

6.  System logs the event “Add group” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Add group failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the group information. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. SS administrator inserted a group code that already exists.
    - 4a.1. System displays the error message “A group with code 'X' already exists” (where “X” is the group code).
    - 4a.2. System logs the event “Add group failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the group code. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].