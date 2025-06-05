#### 3.2.4 UC SERVICE\_32: Add a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actors**: CS administrator

**Brief** **Description**: CS administrator adds a global group to the
central server.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: CS administrator wants to add a global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to add a global group.

2.  CS administrator inserts the code and description of the group.

3.  System parses the user input: 3.2.12.

4.  System verifies that a global group with the inserted code does not
    already exist in the system configuration.

5.  System saves the information about the new global group to the
    system configuration.

6.  System logs the event “Add global group” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the error message “Failed to add global group: 'X'” (where “X” is the termination message from the parsing process).
    - 3a.2. System logs the event “Add global group failed” to the audit log.
    - 3a.3. CS administrator selects to reinsert the group information. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

- 4a. CS administrator inserted a group code that already exists.
    - 4a.1. System displays the error message “Failed to add global group: group code 'X' has already been taken” (where “X” is the group code).
    - 4a.2. System logs the event “Add global group failed” to the audit log.
    - 4a.3. CS administrator selects to reinsert the group code. Use case continues from step 3.
        - 4a.3a. CS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]