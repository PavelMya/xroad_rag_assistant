#### 2.3.3 UC GCONF\_22: Upload a Configuration Anchor File

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator uploads the configuration anchor
file to the system. System displays the details of the anchor and asks
for SS administrator to confirm the upload. After confirmation, the
system verifies that the configuration downloaded from the source
pointed by this anchor is usable and starts using the uploaded anchor.

**Preconditions**: SS administrator has received a configuration anchor
file form the internal configuration provider and validated the
integrity of the anchor.

**Postconditions**: -

**Trigger**: The configuration anchor needs to be uploaded

-   on system initialization or

-   when the X-Road governing agency has notified SS administrator that
    the configuration anchor needs to be updated.

**Main Success Scenario**:

1.  SS administrator selects to upload a configuration anchor file.

2.  SS administrator inserts the path to the anchor file in the local
    file system.

3.  System verifies that the file is a valid configuration anchor file
    by validating the uploaded file against the configuration anchor
    schema.

4.  System verifies that the instance identifier in the anchor file
    corresponds to the instance identifier of the security server.

5.  System calculates and displays the SHA-224 hash value and the
    generation time of the selected anchor file and prompts for
    confirmation.

6.  SS administrator confirms.

7.  System verifies that the anchor file is functional by downloading
    configuration from the source pointed by the anchor: 2.3.4.

8.  System saves the configuration anchor (overwriting the existing
    anchor if such exists).

9.  System logs the event “Upload configuration anchor” to the audit
    log.

**Extensions**:

- 3a. The selected file is not a valid configuration anchor file.
    - 3a.1. System displays the error message: “Configuration anchor import failed: invalid anchor file”.
    - 3a.2. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 3a.2a. SS administrator selects to terminate the use case.

- 4a. The instance identifier in the anchor file does not correspond to the instance identifier of the security server.
    - 4a.1. System displays the error message: “Configuration anchor upload failed: unexpected instance identifier found in anchor”.
    - 4a.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 6a. SS administrator cancels the import.
    - 6a.2. Use case terminates.

- 7a. Downloading of the internal configuration fails.
    - 7a.1. System displays the error message: “Configuration source cannot be reached, check source URL in uploaded anchor file”.
    - 7a.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 7a.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 7a.3a. SS administrator selects to terminate the use case.

- 7b. The downloaded internal configuration is expired.
    - 7b.1. System displays the error message: “Configuration from source is out of date”.
    - 7b.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 7b.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 7b.3a. SS administrator selects to terminate the use case.

- 7c. Verification of the signature value of the downloaded internal configuration failed.
    - 7c.1. System displays the error message: “Signature of configuration cannot be verified”.
    - 7c.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 7c.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 7c.3a. SS administrator selects to terminate the use case.

- 7d. The downloaded internal configuration directory does not contain private parameters.
    - 7d.1. System displays the error message: “Configuration anchor import failed: invalid anchor file”.
    - 7d.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 7d.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 7d.3a. SS administrator selects to terminate the use case.

- 7e. The verification of the downloaded internal configuration fails for reasons other than the ones listed in extensions 7b-d.
    - 7e.1. System displays the error message: “Configuration from source failed verification”.
    - 7e.2. System logs the event “Upload configuration anchor failed” to the audit log.
    - 7e.3. SS administrator selects to reinsert the path to the configuration anchor file. Use case continues from step 3.
        - 7e.3a. SS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[PR-SPEC-AL](#Ref_SPEC-AL)\].

-   The format of the configuration anchor and the configuration
    directory and the protocol for downloading the configuration are
    described in the document “X-Road: Protocol for Downloading
    Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\].