### 3.2 UC SS\_01: Log In to the Graphical User Interface

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor:** SS administrator

**Brief Description:** SS administrator logs in to the graphical user
interface (GUI) of the security server.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wishes to log in to the GUI to view or
manage the security server configuration.

**Main Success Scenario**:

1.  SS administrator selects to log in to the GUI.

2.  SS administrator inserts the user name and password.

3.  System verifies that the system is not currently undergoing the
    system restore process.

4.  System verifies that a user with the inserted user name and password
    is configured in the system configuration and logs the SS
    administrator in to the GUI.

5.  System logs the event “Log in user” to the audit log.

**Extensions**:

- 3a. The system is currently undergoing the system restore process.
    - 3a.1. System displays the error message “Restore in progress, try again later”.
    - 3a.2. System logs the event “Log out user” to the audit log.
    - 3a.3. SS administrator selects to reinsert the user name and/or the password. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The user with the inserted user name does not exist or the password is incorrect.
    - 4a.1. System displays the error message “Authentication failed. Please try again”. The text fields are emptied.
    - 4a.2. System logs the event “Log in user failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the user name and/or the password. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].