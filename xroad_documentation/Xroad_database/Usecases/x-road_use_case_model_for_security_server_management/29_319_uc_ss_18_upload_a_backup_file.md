### 3.19 UC SS\_18: Upload a Backup File

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator uploads a backup file to the
security server.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to upload a backup file.

**Main Success Scenario**:

1.  SS administrator selects to upload a backup file.

2.  SS administrator inserts the path to the file.

3.  System verifies that the name of the file contains valid characters.

4.  System verifies that the uploaded file has valid extension.

5.  System verifies that the content of the uploaded file is in tar
    format.

6.  System verifies that a backup file with the same file name does not
    exist in the system configuration.

7.  System saves the backup file to the system configuration and
    displays the message “New backup file uploaded successfully” to the
    SS administrator.

8.  System logs the event “Upload backup file” to the audit log.

**Extensions**:

- 3a. The file name contains invalid characters.
    - 3a.1. System displays the error message “Failed to upload new backup file: Filename 'X' contains invalid characters. Valid characters include: (A-Z), (a-z), (0-9), (\_), (.), (-).'” (where “X” is the file name of the uploaded file).
    - 3a.2. System logs the event “Upload backup file failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the path to the backup file. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The file has invalid extension.
    - 4a.1. System displays an error message “Failed to upload new backup file: Uploaded file name 'X' has invalid extension, valid one is 'tar'” (where “X” is the name of the uploaded file).
    - 4a.2. System logs the event “Upload backup file failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the path to the backup file. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. The content of the file is not in tar format.
    - 5a.1. System displays the error message “Failed to upload new backup file: Content of uploaded file must be in tar format”.
    - 5a.2. System logs the event “Upload backup file failed” to the audit log.
    - 5a.3. SS administrator selects to reinsert the path to the backup file. Use case continues from step 3.
        - 5a.3a. SS administrator selects to terminate the use case.

- 6a. A backup file with the same file name is saved in the system configuration.
    - 6a.1. System displays the message “Backup file with name 'X' already exists, do you want to overwrite it?” (where “X” is the file name of the uploaded file) and prompts for confirmation.
    - 6a.2. SS administrator confirms. Use case continues from step 7.
        - 6a.2a. SS administrator cancels the upload.
            - 6a.2a.1. SS administrator selects to reinsert the path to the backup file. Use case continues from step 3.
                - 6a.2a.1a. SS administrator selects to terminate the use case.

**Related information**:

-   Backup files are located at /var/lib/xroad/backup.

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].