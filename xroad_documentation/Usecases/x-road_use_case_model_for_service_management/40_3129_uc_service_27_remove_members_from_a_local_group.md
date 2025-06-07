#### 3.1.29 UC SERVICE\_27: Remove Members from a Local Group

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator removes group members from a
local group. The access rights granted for the group will not be
available for the removed group members.

**Preconditions**: -

**Postconditions**:

-   Group members have been removed from the local group.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to remove group members from a local
group.

**Main** **Success** **Scenario**:

1.  SS administrator selects to remove subjects from a local group.

2.  SS administrator selects group members and removes them from the
    local group.

3.  System removes group members from the local group. The access rights
    granted for the group will not be available for the removed group
    members.

4.  System logs the event “Remove members from group” to the audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].