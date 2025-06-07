#### 3.2.10 UC SERVICE\_38: Remove an X-Road Member or Subsystem from a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actor**: CS administrator

**Brief** **Description**: CS administrator removes an X-Road member or
a member's subsystem from a global group.

**Preconditions**: -

**Postconditions**:

-   The X-Road member or subsystem is removed from a global group and
    loses the access rights granted for this group in the security
    servers.

-   An audit log record for the event is created.

**Trigger**: CS administrator wants to remove an X-Road member or a
member's subsystem from a global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to remove an X-Road member or a subsystem
    from a global group.

2.  System removes the member or member's subsystem from the global
    group and displays the message: “Member 'X' successfully deleted
    from global group 'Y'”, where “X” is the member code of the X-Road
    member and “Y” is the global group code.

3.  System logs the event “Remove member from global group” to the audit
    log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].