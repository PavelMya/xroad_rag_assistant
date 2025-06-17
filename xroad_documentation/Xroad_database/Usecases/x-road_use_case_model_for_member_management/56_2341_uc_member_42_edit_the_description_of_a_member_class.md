#### 2.3.41 UC MEMBER\_42: Edit the Description of a Member Class

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator changes the description of a member class.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to edit the description of a member class.

2.  CS administrator inserts the description.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

4.  System verifies that no other member class with the inserted description exist in the system configuration.

5.  System saves the member class description.

6.  System logs the event “Edit member class description” to the audit log.

**Extensions**:

3a. The parsing of the user input terminated with an error.

  - 3a.1. System displays the termination message of the parsing process.

  - 3a.2. System logs the event “Edit member class description failed” to the audit log.

  - 3a.3. CS administrator selects to reinsert the description. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

4a. A member class with the inserted description already exists in the system configuration.

  - 4a.1. System displays the error message: “description 'X' has already been taken”, where “X” is the description of the group.

  - 4a.2. System logs the event “Edit member class description failed” to the audit log.

  - 4a.3. CS administrator selects to reinsert the description. Use case continues from step 3.

    - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].