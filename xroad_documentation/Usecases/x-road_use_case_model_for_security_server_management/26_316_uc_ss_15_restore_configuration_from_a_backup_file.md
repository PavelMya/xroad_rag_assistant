### 3.16 UC SS\_15: Restore Configuration from a Backup File

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator restores the security server
configuration from a backup file stored in the system configuration.

**Preconditions**: The backup file exists in the system configuration.

**Postconditions**: -

**Trigger**: SS administrator wants to restore the security server
configuration to a previously backed up state.

**Main Success Scenario**:

1.  SS administrator selects to restore security server configuration
    from a backup file saved in the system configuration.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System runs the script, that

    a.  verifies that the file is a valid backup file;

    b.  verifies the label of the backup file:

    -   verifies that the server type in the label corresponds to
        the type of the server that is being restored;

        *Note: System verifies only the server type and ignores the rest of  the information in the label in case the restore script is called from  the CLI with the -F option.*
    
    -   verifies that the server software version in the label is compatible
        with the installed software version of the server that is being
        restored;
    
    -   verifies that the security server identifier in the label
        corresponds to the identifier of the security server that is being
        restored;
    
    c.  clears shared memory;
    
    d.  stops all system services, except for xroad-proxy-ui-api;
    
    e.  creates a pre-restore backup of the system configuration (step 2 of
        3.15) to /var/lib/xroad/conf\_prerestore\_backup.tar (the
        pre-restore backup file is overwritten on each restore);
    
    f.  deletes the content of the following directory:
    
        -   /etc/xroad/
        
    g.  writes the database dump from the backup file to
        /var/lib/xroad/dbdump.dat;

    h.  restores the content of the directory /etc/xroad/ from the backup file;

    i.  restores the database data (including the schema) from the dump
        file /var/lib/xroad/dbdump.dat;

    j.  restarts all the services that were previously stopped.

5.  System displays the message “Configuration restored successfully
    from file 'X'.” (where “X” is the name of the backup file) and the
    restore script output to the SS administrator.

6.  System notifies the SS administrator: “During restore, security
    tokens were logged out from.”

7.  System logs the event “Restore configuration” to the audit log.

**Extensions**:

- 3a. SS administrator cancels the restoring of the configuration from the backup file.
    - 3a.1. Use case terminates.

- 4a. Restoring the security server configuration failed.
    - 4a.1. System displays the error message “Restoring configuration from file 'X' failed.” (where X is the file name of the backup file) and the output of the restore script.
    - 4a.2. System logs the event “Restore configuration failed” to the audit log.
    - 4a.3. Use case terminates.

**Related information**:

-   Backup files are located at /var/lib/xroad/backup.

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].