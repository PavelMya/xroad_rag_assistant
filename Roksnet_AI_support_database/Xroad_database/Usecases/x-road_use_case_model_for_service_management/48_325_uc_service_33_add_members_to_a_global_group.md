#### 3.2.5 UC SERVICE\_33: Add Members to a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actors**: CS administrator

**Brief** **Description**: CS administrator adds members (X-Road members
or subsystems) to the global group. Added group members will inherit all
access rights granted for the group.

**Preconditions**: The subjects are not members of this group.

**Postconditions**:

-   Group members have been added to the global group.

-   An audit log record for the event is created.

**Trigger**: CS administrator wants to add members to the global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to add group members to the global group.

2.  CS administrator selects subjects and adds them to the global group.
    It is possible to add only those subjects that are not already
    members of this group.

3.  System adds group members to the global group. Added group members
    will inherit all access rights granted for the group.

4.  System logs the event “Add members to global group” to the audit
    log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\]