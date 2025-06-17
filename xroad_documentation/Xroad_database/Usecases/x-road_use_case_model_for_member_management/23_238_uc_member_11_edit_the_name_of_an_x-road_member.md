#### 2.3.8 UC MEMBER\_11: Edit the Name of an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief description**: CS administrator edits the name of an X-Road member.

**Precondition**: -

**Postcondition**: An audit log record for the event is created.

**Trigger**: The name of an X-Road member needs to be changed.

**Main success scenario**:

1.  CS administrator selects to edit the name of an X-Road member.

2.  CS administrator inserts the name.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

4.  System saves the changes.

5.  System logs the event “Edit member name” to the audit log.

**Extensions**:

3a. The parsing of the user input terminated with an error message.

- 3a.1. System displays the error message: “Failed to edit member: X”, where X is the termination message of the parsing process.

- 3a.2. System logs the event “Edit member name failed” to the audit log.

- 3a.3. CS administrator selects to reinsert the member information. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

**Related information:**

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].