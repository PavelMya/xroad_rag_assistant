#### 3.1.31 UC SERVICE\_29: Delete a Local Group

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator deletes a local group. The
access rights that were granted for the group will not be available for
the X-Road subsystems that were the members of this group.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to delete a local group.

**Main** **Success** **Scenario**:

1.  SS administrator selects to delete a local group.

2.  System prompts for confirmation to delete the local group.

3.  SS administrator confirms.

4.  System deletes the local group from the system configuration. The
    access rights that were granted for the group will not be available
    for the X-Road subsystems that were the members of this group.

5.  System logs the event “Delete group” to the audit log.

**Extensions**:

3a. SS administrator terminates the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]