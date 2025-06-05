#### 2.3.40 UC MEMBER\_41: Add a Member Class

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator adds a member class.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: A member class needs to be described for this X-Road instance.

**Main Success Scenario**:

1.  CS administrator selects to add a member class.

2.  CS administrator inserts the code and description for the member class.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input);

4.  System converts the inserted member class code to uppercase and verifies that no other member class with the inserted code and/or description exists in the system configuration.

5.  System saves the member class information.

6.  System logs the event “Add member class” to the audit log.

**Extensions**:

3a. The parsing of the user input terminated with an error.

  - 3a.1. System displays the termination message of the parsing process.

  - 3a.2. System logs the event “Add member class failed” to the audit log.

  - 3a.3. CS administrator selects to reinsert member class information. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

4a. A member class with the inserted code already exists in the system configuration.

  - 4a.1. System displays the error message: “Member class with the same code already exists”.

  - 4a.2. System logs the event “Add member class failed” to the audit log.

  - 4a.3. CS administrator selects to reinsert member class information. Use case continues from step 3.

    - 4a.3a. CS administrator selects to terminate the use case.

4b. A member class with the inserted description already exists in the system configuration.

  - 4b.1. System displays the error message: “description 'X' has already been taken”, where “X” is the description of the group.

  - 4b.2. System logs the event “Add member class failed” to the audit log.

  - 4b.3. CS administrator selects to reinsert member class information. Use case continues from step 3.

    - 4b.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].