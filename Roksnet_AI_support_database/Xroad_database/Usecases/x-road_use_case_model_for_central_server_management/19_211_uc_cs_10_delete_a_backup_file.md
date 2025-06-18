### 2.11 UC CS\_10: Delete a Backup File

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes a backup file.

**Preconditions**: A backup file is saved in the system configuration.

**Postconditions**: -

**Trigger**: CS administrator wants to delete a backup file.

**Main Success Scenario**:

1.  CS administrator selects to delete a backup file.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System deletes the backup file and displays the message “Selected
    backup deleted successfully”.

5.  System logs the event “Delete backup file” to the audit log.

**Extensions**:

- 3a. CS administrator cancels the deleting of the backup file.
    - 3a.1. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].