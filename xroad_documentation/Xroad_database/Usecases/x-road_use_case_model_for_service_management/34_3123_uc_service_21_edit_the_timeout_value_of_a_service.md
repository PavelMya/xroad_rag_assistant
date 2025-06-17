#### 3.1.23 UC SERVICE\_21: Edit the Timeout Value of a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the service timeout
value.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to change the service timeout value.

**Main** **Success** **Scenario**:

1.  SS administrator selects to edit the timeout value of a service.

2.  SS administrator inserts the timeout value.

3.  System parses the user input: 3.1.13.

4.  System verifies that the inserted value is in valid format.

5.  System saves the inserted service timeout value to the system
    configuration.

6.  System logs the event “Edit service parameters” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the termination message from the parsing process.
    - 3a.2. System logs the event “Edit service parameters failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the timeout value. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The inserted timeout value is 0.
    - 4a.1. System displays a warning message “A timeout value of zero is interpreted as an infinite timeout.” and asks for confirmation for continuing.
    - 4a.2. SS administrator selects to reinsert the timeout value. Use case continues from step 3.
        - 4a.2a. SS administrator selects to terminate the use case.
        - 4a.2b. SS administrator chooses to continue.
            - 4a.2b.1. Use case continues from step 5.

- 4b. The inserted timeout value is not a positive integer.
    - 4b.1. System displays the error message “Timeout value must be a positive integer.”
    - 4b.2. System logs the event “Edit service parameters failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the timeout value. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].