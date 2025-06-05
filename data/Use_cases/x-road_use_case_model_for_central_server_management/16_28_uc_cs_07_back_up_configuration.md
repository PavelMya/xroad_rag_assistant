### 2.8 UC CS\_07: Back Up Configuration

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator backs up the central server
configuration.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Triggers**: CS administrator wants to back up the central server
configuration.

**Main Success Scenario**:

1.  CS administrator selects to back up the central server
    configuration.

2.  System runs the backup script that

    a.  creates the database dump file (to /var/lib/xroad/dbdump.dat)
        containing the contents of the central server database. The
        schema\_migrations table and the database schema are excluded
        from the database dump;

    b.  creates the backup file containing the database dump file and
        the following directories:

    -   /etc/xroad/

    -   /etc/nginx/sites-enabled/
    
    and includes the following information as a label in the created .tar file:

    -   the type of the server (“central” for central servers),
    
    -   the version of the central server software,
    
    -   the X-Road instance identifier,
    
    -   the node name if the central server is a part of a high availability
    
        cluster;

    c.  saves the created backup file to the directory
        /var/lib/xroad/backup.

3.  System displays the message “Configuration backup created” and the
    output of the backup script.

4.  System logs the event “Back up configuration” to the audit log.

**Extensions**:

- 3a. Backing up the central server configuration failed.
    - 3a.1  Backup script produces an error code that prompts the error handling to remove any incomplete backup archives
    - 3a.2. System displays the error message “Error making configuration backup, script exited with status code 'X'” (where “X” is the exit code of the backup script) and the output of the backup script.
    - 3a.3. System logs the event “Back up configuration failed” to the audit log.
    - 3a.4. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].