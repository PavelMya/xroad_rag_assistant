#### 2.3.7 UC MEMBER\_10: Add an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief description**: CS administrator registers an organization as an X-Road member.

**Preconditions**:

-   The organization has entered into an X-Road membership contract with the X-Road governing agency.

-   At least one member class is described in the system configuration.

**Postcondition**: An audit log record for the event is created.

**Trigger:** An organization has been approved for joining the X-Road by the X-Road governing authority.

**Main success scenario**:

1.  CS administrator selects to add an X-Road member.

2.  CS administrator inserts the following information:

    -   the name of the organization;

    -   the X-Road member class of the organization and

    -   the X-Road member code of the organization.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

4.  System verifies that an organization with the inserted member class and member code combination is not already an X-Road member.

5.  System saves the added X-Road member information to system configuration.

6.  System displays the message: “Successfully added X-Road member with member class 'X' and member code 'Y'.”, where “X” is the inserted member class and “Y” the inserted member code.

7.  System logs the event “Add member” to the audit log.

**Extensions:**

3a. The parsing of the user input terminated with an error message.

- 3a.1. System displays the error message: “Failed to add member: X”, where X is the termination message of the parsing process.

- 3a.2. System logs the event “Add member failed” to the audit log.

- 3a.3. CS administrator selects to reinsert the member information. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

4a. An X-Road member with the inserted member class and member code combination already exists.

- 4a.1. System displays the error message “Failed to add member: Member with class X and code Y already exists”, where “X” is the X-Road member class and “Y” is the X-Road member code that was inserted.

- 4a.2. System logs the event “Add member failed” to the audit log.

- 4a.3 CS administrator selects to reinsert the member information. Use case continues from step 3.

    - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].