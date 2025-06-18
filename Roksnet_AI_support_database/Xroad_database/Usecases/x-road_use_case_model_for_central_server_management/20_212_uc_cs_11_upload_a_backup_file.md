### 2.12 UC CS\_11: Upload a Backup File

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator uploads a backup file to the
central server.

**Preconditions**: -

**Postconditions**: -

**Trigger**: CS administrator wants to upload a backup file.

**Main Success Scenario**:

1.  CS administrator selects to upload a backup file.

2.  CS administrator selects the file from the local file system.

3.  System verifies that the file name contains valid characters.

4.  System verifies that the extension of the uploaded file is .tar.

5.  System verifies that the content of the uploaded is in tar format.

6.  System verifies that a backup file with the same file name does not
    exist in the system configuration.

7.  System saves the backup file to the system configuration and
    displays the message “New backup file uploaded successfully”.

8.  System logs the event “Upload backup file” to the audit log.

**Extensions**:

- 3a. The file name contains invalid characters.
    - 3a.1. System displays the error message “Failed to upload new backup file: Filename 'X' contains invalid characters. Valid characters include: (A-Z), (a-z), (0-9), (\_), (.), (-).'” (where “X” is the file name of the uploaded file).
    - 3a.2. System logs the event “Upload backup file failed” to the audit log.
    - 3a.3. CS administrator selects to reselect the backup file. Use casecontinues from step 3.
    - 3a.3a. CS administrator selects to terminate the use case.

- 4a. The file extension is not .tar.
    - 4a.1. System displays the error message “Failed to upload new backup file: Uploaded file name 'X' has an invalid extension, the only valid one is 'tar'” (where “X” is the file name of the uploaded file).
    - 4a.2. System logs the event “Upload backup file failed” to the audit log.
    - 4a.3. CS administrator selects to reselect the backup file. Use case continues from step 3.
    - 4a.3a. CS administrator selects to terminate the use case.

- 5a. The content of the file is not in valid format.
    - 5a.1. System displays the error message “Failed to upload new backup file: Content of uploaded file must be in tar format”.
    - 5a.2. System logs the event “Upload backup file failed” to the audit log.
    - 5a.3. CS administrator selects to reselect the backup file. Use casecontinues from step 3.
    - 5a.3a. CS administrator selects to terminate the use case.

- 6a. A backup file with the same file name is saved in the system configuration.
    - 6a.1. System displays the message “Backup file with name 'X' alreadyexists, do you want to overwrite it?” (where “X” is the file name ofthe uploaded file) and prompts for confirmation.
    - 6a.2. CS administrator confirms. Use case continues from step 7.
    - 6a.2a. CS administrator cancels the upload.
    - 6a.2a.1. CS administrator selects to reselect the backup file. Use case continues from step 3.
    - 6a.2a.1a. CS administrator selects to terminate the use case.

**Related information**:

-   The backup files are saved to /var/lib/xroad/backup.

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].