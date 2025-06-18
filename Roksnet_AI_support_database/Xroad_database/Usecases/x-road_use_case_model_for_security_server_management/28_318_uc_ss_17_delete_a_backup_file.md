### 3.18 UC SS\_17: Delete a Backup File

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator deletes a backup file.

**Preconditions**: A backup file is saved in the system configuration.

**Postconditions**: -

**Trigger**: SS administrator wants to delete a backup file.

**Main Success Scenario**:

1.  SS administrator selects to delete a backup file.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System deletes the backup file and displays the message “Selected
    backup deleted successfully” to the SS administrator.

5.  System logs the event “Delete backup file” to the audit log.

**Extensions**:

- 3a. SS administrator cancels the deleting of the backup file.
    - 3a.1. Use case terminates.

**Related information**: -

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].