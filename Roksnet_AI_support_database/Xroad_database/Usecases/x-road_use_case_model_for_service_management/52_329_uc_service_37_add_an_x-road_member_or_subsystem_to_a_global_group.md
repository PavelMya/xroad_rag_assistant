#### 3.2.9 UC SERVICE\_37: Add an X-Road Member or Subsystem to a Global Group

**System**: Central server

**Level**: User task

**Component**: Central server

**Actor**: CS administrator

**Brief** **Description**: CS administrator adds an X-Road member or a
member's subsystem to a global group.

**Preconditions**: One or more global groups have been created in the
central server.

**Postconditions**:

-   The X-Road member or subsystem is a member of a global group and
    inherits the access rights granted for this group in the security
    servers.

-   An audit log record for the event is created.

**Trigger**: CS administrator wants to add an X-Road member or a
member's subsystem to a global group.

**Main** **Success** **Scenario**:

1.  CS administrator selects to add an X-Road member or a member's
    subsystem to a global group.

2.  CS administrator selects whether to add the X-Road member or the
    subsystem of the member and selects the global group from the list
    of global groups to which the member or selected subsystem does not
    already belong to.

3.  System adds the member or member's subsystem to the selected global
    group and displays the message: “Member 'X' successfully added to
    global group 'Y'”, where “X” is the member code of the X-Road member
    and “Y” is the global group code.

4.  System logs the event “Add member to global group” to the audit log.

**Extensions**: -

-   Related information:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].