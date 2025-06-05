#### 3.1.30 UC SERVICE\_28: Edit the Description of a Local Group

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the description of a
local group.

**Preconditions**: A local group has been created.

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to change the description of a local
group.

**Main** **Success** **Scenario**:

1.  SS administrator selects to edit the description of a local group.

2.  SS administrator inserts the description.

3.  System parses the user input: 3.1.13.

4.  System saves the local group description to the system
    configuration.

5.  System logs the event “Edit group description” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the termination message from the parsing process.
    - 3a.2. System logs the event “Edit group description failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the group description. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]