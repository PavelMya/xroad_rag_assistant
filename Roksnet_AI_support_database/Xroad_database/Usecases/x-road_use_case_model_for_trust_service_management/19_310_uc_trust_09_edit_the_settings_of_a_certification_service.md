### 3.10 UC TRUST\_09: Edit the Settings of a Certification Service

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator edits the settings of a
certification service.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Trigger**: The usage restrictions for certificates issued by the
certification service, or the class name that describes the certificate
profile for the certification service, need to be set or changed.

**Main Success Scenario**:

1.  CS administrator selects to edit the settings of a certification
    service.

2.  CS administrator

    -   selects whether the certificates issued by the certification
        service can be used only for authentication or also for signing;

    -   inserts the fully qualified name of the Java class that
        describes the certificate profile for the certification service.

3.  System parses the user input: 3.20.

4.  System verifies, that the Java class that describes the certificate
    profile exists in the system's classpath and saves the changes.

5.  System logs the event “Edit certification service settings” to the
    audit log.

**Extensions**:

- 3a. The parsing of the user input terminated with an error message.
    - 3a.1. System displays the termination message of the parsing process.
    - 3a.2. System logs the event “Edit certification service settings failed” to the audit log.
    - 3a.3. CS administrator selects to reinsert the certificate profile class name. Use case continues from step 3.
        - 3a.3a. CS administrator selects to terminate the use case.

- 4a. System did not find the inserted certificate profile class on the classpath.
    - 4a.1. System displays the error message “Certificate profile with name 'X' does not exist.”, where “X” is the inserted class name.
    - 4a.2. System logs the event “Edit certification service settings failed” to the audit log.
    - 4a.3. CS administrator selects to reinsert the certificate profile class name. Use case continues from step 3.
        - 4a.3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].