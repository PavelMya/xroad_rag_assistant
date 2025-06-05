### 3.4 UC SS\_03: Log a User Out of the Graphical User Interface

**System**: Security server

**Level**: System task

**Component:** Security server

**Actor**: -

**Brief Description**: System logs the user out of the GUI when the
logged in user has been idle for 30 minutes.

**Preconditions**: -

**Postconditions**: User is logged out of the GUI.

**Triggers**: The logged in user has been idle for 30 minutes.

**Main Success Scenario**:

1.  User has been idle for 30 minutes.

2.  System displays the dialog “Session expired - You have been idle for 30 minutes and your session has expired. For security reasons, you will be logged out.”
 
3.  System logs the SS administrator out of the GUI and redirects the user to the Log-in view.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].