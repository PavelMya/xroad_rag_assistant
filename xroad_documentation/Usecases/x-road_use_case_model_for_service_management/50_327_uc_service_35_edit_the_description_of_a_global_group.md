#### 3.2.7 UC SERVICE\_35: Edit the Description of a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actors**: CS administrator

**Brief** **Description**: CS administrator changes the description of
the global group.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: CS administrator wants to change the description of a
global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to edit the description of a global group.

2.  CS administrator inserts the description.

3.  System parses the user input: 3.1.13.

4.  System saves the global group description to the system
    configuration.

5.  System logs the event “Edit global group description” to the audit
    log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the error message “'X'” (where “X” is the termination message from the parsing process).
    - 3a.2. System logs the event “Edit global group description failed” to the audit log.
    - 3a.3. CS administrator selects to reinsert the group description. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]