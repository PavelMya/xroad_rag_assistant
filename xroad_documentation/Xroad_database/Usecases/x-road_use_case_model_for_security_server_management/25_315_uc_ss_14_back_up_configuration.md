### 3.15 UC SS\_14: Back Up Configuration

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator backs up the security server
configuration.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to back up the security server
configuration.

**Main Success Scenario**:

1.  SS administrator selects to back up the security server
    configuration.

2.  System runs the backup script, that

    a.  creates a dump file of the database (including the schema) to
        the location /var/lib/xroad/dbdump.dat, that contains the
        contents of the security server database;

    b.  creates the backup file containing the database dump file and
        the following directory:

    -   /etc/xroad/
    
    and includes the following information as a label in the created .tar file:
    
    -   the type of the server (“security” for security servers),
    
    -   the version of the security server software,
    
    -   the X-Road identifier of the security server;

    c.  saves the created backup file to /var/lib/xroad/backup.

3.  System displays the message “Configuration backup created” and the
    backup script output to the SS administrator.

4.  System logs the event “Back up configuration” to the audit log.

**Extensions**:

- 3a. Backing up the security server configuration failed.
    - 3a.1  Backup script produces an error code that prompts the error handling to remove any incomplete backup archives
    - 3a.2. System displays the error message “Error making configuration backup, script exited with status code 'X'” (where “X” is the exit code of the backup script) and the output of the backup script.
    - 3a.3. System logs the event “Back up configuration failed” to the audit log.
    - 3a.4. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].