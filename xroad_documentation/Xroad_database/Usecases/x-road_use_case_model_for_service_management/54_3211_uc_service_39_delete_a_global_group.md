#### 3.2.11 UC SERVICE\_39: Delete a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actors**: CS administrator

**Brief** **Description**: CS administrator deletes a global group. The
access rights that were granted for the group will not be available for
the X-Road members and subsystems that were the members of this group.

**Preconditions**: A global group has been created.

**Postconditions**: -

**Trigger**: CS administrator wants to delete a global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to delete a global group.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System deletes the global group from the system configuration.

5.  System logs the event “Delete global group” to the audit log.

**Extensions**:

- 3a. CS administrator terminates the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].