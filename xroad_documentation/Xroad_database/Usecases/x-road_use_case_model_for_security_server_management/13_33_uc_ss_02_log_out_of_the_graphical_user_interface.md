### 3.3 UC SS\_02: Log Out of the Graphical User Interface

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator logs out of the GUI.

**Preconditions**: -

**Postconditions**:

-   SS administrator is logged out of the GUI.

-   An audit log record for the event is created.

**Triggers**: SS administrator wishes to log out of the GUI.

**Main Success Scenario**:

1.  SS administrator selects to log out of the GUI (Profile Menu > Log out).

2.  System logs the SS administrator out of the GUI and redirects the user to the Log-in view.

3.  System logs the event “Log out user” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].