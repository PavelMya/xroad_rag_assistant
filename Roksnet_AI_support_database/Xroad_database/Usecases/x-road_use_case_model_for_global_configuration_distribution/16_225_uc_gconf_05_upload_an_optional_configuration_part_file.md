#### 2.2.5 UC GCONF\_05: Upload an Optional Configuration Part File

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator uploads an optional
configuration part file.

**Preconditions**: Optional configuration part data is described in the
system (see 2.2.4).

**Postconditions**: An audit log record for the event has been created.

**Trigger**: The contents of the optional configuration part file have
been changed and CS administrator wants to upload the updated file to
the system.

**Main Success Scenario**:

1.  CS administrator selects to upload an optional configuration part
    file.

2.  CS administrator inserts the path to the configuration part file in
    the computer's file system.

3.  System verifies that the uploaded file conforms to xsd schema for 
    given content identifier.

4.  System displays the message “Configuration file for content
    identifier 'X' uploaded successfully.”, where “X” is the
    content-identifier described for the configuration part.

5.  System verifies that a file for this optional configuration part
    already exists in the system configuration and replaces the existing
    file with the uploaded one.

6.  System logs the event “Upload configuration part” to the audit log.

**Extensions**:

- 3a. A validator is not described for this configuration part.
    - 3a.1. Use case continues from step 5.

- 3b. The system is unable to find the described validation program.
    - 3b.1. System displays the error message: “Failed to upload configuration part: Validation program 'X' does not exist in the file system.”, where “X” is the validation program path described for this configuration part.
    - 3b.2. System logs the event “Upload configuration part failed” to the audit log.
    - 3b.3. CS administrator selects to reinsert the path to the configuration part file. Use case continues from step 3.
        - 3b.3a. CS administrator selects to terminate the use case.

- 3c. The communication with the validation program closed unexpectedly.
    - 3c.1. System displays the error message: “Validation program 'X' ended prematurely, make sure if it does the right thing.”, where “X” is the validation program path described for this configuration part.
    - 3c.2. System logs the event “Upload configuration part failed” to the audit log.
    - 3c.3. CS administrator selects to reinsert the path to the configuration part file. Use case continues from step 3.
        - 3c.3a. CS administrator selects to terminate the use case.

- 3d. An error occurred while running the validation program.
    - 3d.1. System displays the error message: “IO error occurred when running validation program 'X', message: 'Y'”, where “X” is the validation program path described for this configuration part and “Y” is the description of the error.
    - 3d.2. System logs the event “Upload configuration part failed” to the audit log.
    - 3d.3. CS administrator selects to reinsert the path to the configuration part file. Use case continues from step 3.
        - 3d.3a. CS administrator selects to terminate the use case.

- 4a. The validation succeeded with validation errors.
    - 4a.1. System displays the error message: “Failed to upload configuration part: Validation of configuration file with content identifier 'X' failed.”, where “X” is the content identifier of the optional configuration part CS administrator chose to upload, and the validation errors.
    - 4a.2. System logs the event “Upload configuration part failed” to the audit log.
    - 4a.3. CS administrator selects to reinsert the path to the configuration part file. Use case continues from step 3.
        - 4a.3a. CS administrator selects to terminate the use case.

- 4b. The validation succeeded with validation warnings.
    - 4b.1. System displays the message: “Configuration file for content identifier 'X' uploaded with some warnings.”, where “X” is the content identifier of the optional configuration part CS administrator chose to upload, and the validation warnings.
    - 4b.2. Use case continues from step 6.

- 6a. No previous file for this optional part exists in the system's database.
    - 6a.1. System saves the uploaded file.

**Related information**:

-   The uploaded file is distributed to the configuration clients as a
    part of the internal configuration.

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[PR-GCONF](#Ref_PR-GCONF)\].