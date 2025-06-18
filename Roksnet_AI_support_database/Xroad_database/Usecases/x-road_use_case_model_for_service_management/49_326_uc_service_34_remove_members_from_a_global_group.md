#### 3.2.6 UC SERVICE\_34: Remove Members from a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actors**: CS administrator

**Brief** **Description**: CS administrator removes members from a
global group. The access rights granted for the group will not be
available for the removed members.

**Preconditions**: -

**Postconditions**:

-   The group members have been removed from the global group.

-   An audit log record for the event is created.

**Trigger**: CS administrator wants to remove group members from a
global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to remove subjects from global group.

2.  CS administrator selects the subjects to be removed from the group.

3.  System removes the selected members from the global group. The
    access rights granted for the group will not be available for the
    removed members.

4.  System logs the event “Remove members from global group” to the
    audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].