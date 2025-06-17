#### 2.3.11 UC MEMBER\_56: Add a Subsystem to an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief description**: CS administrator adds a subsystem to an X-Road member.

**Preconditions**: -

**Postcondition**: An audit log record for the event is created.

**Trigger:** -

**Main success scenario**:

1.  CS administrator selects to add a subsystem to an X-Road member.

2.  CS administrator inserts the code of the subsystem.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

4.  System verifies that a subsystem with the inserted code is not already saved for this X-Road member in the system configuration.

5.  System saves the added subsystem to system configuration.

6.  System logs the event “Add subsystem” to the audit log.

**Extensions:**

3a. The parsing of the user input terminated with an error message.

  - 3a.1. System displays the termination message of the parsing process.

  - 3a.2. System logs the event “Add subsystem failed” to the audit log.

  - 3a.3. CS administrator selects to reinsert the subsystem code. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

4a. The X-Road member already has a subsystem with the inserted code.

  - 4a.1. System displays the error message “Failed to add subsystem: Subsystem 'X' already exists”, where “X” is the inserted subsystem code.

  - 4a.2. System logs the event “Add subsystem failed” to the audit log.

  - 4a.3 CS administrator selects to reinsert the member information. Use case continues from step 3.

    - 4a.3a. CS administrator selects to terminate the use case.

**Related information:**

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].