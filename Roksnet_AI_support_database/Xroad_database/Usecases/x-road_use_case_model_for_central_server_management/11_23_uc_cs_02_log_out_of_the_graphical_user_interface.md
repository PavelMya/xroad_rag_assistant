### 2.3 UC CS\_02: Log Out of the Graphical User Interface

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator logs out of the GUI.

**Preconditions**: -

**Postconditions**:

-   CS administrator is logged out of the GUI.

-   An audit log record for the event has been created.

**Trigger**: CS administrator wants to log out of the GUI.

**Main Success Scenario**:

1.  CS administrator selects to log out of the GUI.

2.  System logs CS administrator out of the GUI.

3.  System logs the event “Log out user” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].