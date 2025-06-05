#### 2.3.42 UC MEMBER\_43: Delete a Member Class

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes a member class that is not used by any of the X-Road members.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: A member class that no longer has any members or was erroneously added needs to be deleted.

**Main Success Scenario**:

1.  CS administrator selects to delete a member class.

2.  System verifies that no X-Road members belong to the member class.

3.  System deletes the member class from the system configuration.

4.  System logs the event “Delete member class” to the audit log.

**Extensions**:

2a. One or more X-Road members belong to the member class.

  - 2a.1. System displays the error message: “Cannot delete member class Z: found X-Road members belonging to the class. Only classes with no registered members can be deleted.”, where “Z” is the code of the member class.

  - 2a.2. System logs the event “Delete member class failed” to the audit log.

  - 2a.3. Use case terminates.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].