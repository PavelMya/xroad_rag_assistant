#### 2.3.20 UC MEMBER\_22: Edit the Address of a Security Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator changes the address of a security server.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to edit the address of a security server.

2.  CS administrator inserts the new address.

3.  System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input).

4.  System verifies that the inserted address is a valid DNS name or IP address.

5.  System saves the inserted value.

6.  System logs the event “Edit security server address” to the audit log.

**Extensions**:

3a. The parsing of the user input terminated with an error message.

  - 3a.1. System displays the termination message of the parsing process.

  - 3a.2. System logs the event “Edit central server address failed” to the audit log.

  - 3a.3. CS administrator selects to reinsert the address. Use case continues from step 3.

    - 3a.3a. CS administrator selects to terminate the use case.

4a. The inserted address is not a valid DNS name or IP address.

  - 4a.1. System displays the error message “Central server address must be DNS name or IP address”.

  - 4a.2. System logs the event “Edit central server address failed” to the audit log.

  - 4a.3. CS administrator selects to reinsert the address. Use case continues from step 3.

    - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].