#### 3.1.28 UC SERVICE\_26: Add Members to a Local Group

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator adds members (X-Road
members' subsystems) to a security server client's local group. Added
group members will inherit all access rights granted for the group.

**Preconditions**: The subjects to be added are not members of this
group.

**Postconditions**:

-   Group members have been added to the local group.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to add group members to the local
group.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add group members to the local group.

2.  SS administrator selects subsystems and adds them to the local
    group. It is possible to add only X-Road members' subsystems to the
    group and it is possible to add only those subsystems that are not
    already members of this group.

3.  System adds group members to the local group. Added group members
    will inherit all access rights granted for the group.

4.  System logs the event “Add members to group” to the audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]