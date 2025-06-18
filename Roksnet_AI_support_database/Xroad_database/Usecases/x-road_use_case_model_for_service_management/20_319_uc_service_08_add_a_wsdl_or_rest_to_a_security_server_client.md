#### 3.1.9 UC SERVICE\_08: Add a WSDL or REST to a Security Server Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator adds a WSDL or a REST to a security
server client (a WSDL or a REST can only be added to a subsystem). System gets
service descriptions from the WSDL or the REST.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to add WSDL or REST for a security server
client.

**Main** **Success** **Scenario**:

1.  SS administrator selects to add a WSDL or a REST.

2.  SS administrator inserts the URL of the WSDL or REST.

3.  System parses the user input: 3.1.13.

4.  System verifies that the inserted URL does not already exist in the
    list of WSDL or REST URLs saved in the system configuration for this client.

5.  System downloads the WSDL or REST file from the URL and reads service
    information from the downloaded file: 3.1.11.

6.  System verifies that the location of a WSDL or a REST validation program is
    described by the system parameter *wsdl-validator-command* or *rest-validator-command* and
    validates the WSDL or REST file using the validator: 3.1.12.

7.  System verifies that none of the services saved for this security
    server client in the system configuration have the same service code
    and service version value combination as any of the services read
    from the downloaded WSDL or REST file.

8.  System saves the WSDL or REST URL and sets the state of the WSDL or REST to
    “disabled” with the default disable message: “Out of order”.

9.  System saves the services read from the WSDL or REST file and sets the
    following default values for each of the services:

    -   service timeout value is set to 60 seconds;

    -   if the protocol part of the URL of the service is “https” then
        the value for TLS certification verification is set to “true”.

10. System logs the event “Add service description" to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the error message “X” (where “X” is the termination message from the parsing process).
    - 3a.2. System logs the event “service description failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The inserted URL already exists.
    - 4a.1. System displays the error message “Failed to add WSDL: WSDL address already exists.” or “Failed to add REST: REST address already exists.”.
    - 4a.2. System logs the event “Add service description failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. The process of downloading and parsing the WSDL or REST file terminated with an error message.
    - 5a.1. System displays the error message “Failed to add WSDL (or REST): X” (where “X” is the termination message from the downloading and parsing process).
    - 5a.2. System logs the event “Add service description failed” to the audit log.
    - 5a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 5a.3a. SS administrator selects to terminate the use case.

- 6a. The location of the WSDL or REST validator is not set.
    - 6a.1. System skips the process of validation.
    - 6a.2. Use case continues from step 7.

- 6b. The process of validating the WSDL or REST file was terminated with an error message.
    - 6b.1. System displays the WSDL or REST validator output describing the reason of the failure, and the error message from the validation process.
    - 6b.2. System logs the event “Add service description failed” to the audit log.
    - 6b.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 6b.3a. SS administrator selects to terminate the use case.

- 6c. The process of validating the WSDL or REST file was finished with a warning message.
    - 6c.1. System prompts the warning message from the validation process. “WSDL ('X') validation gave the following warnings: 'Y'. Do you want to continue? (where “X” is the URL of the WSDL or REST and “Y” is the message from the validation process).
    - 6b.2. System logs the event “Add service description failed” to the audit log.
    - 6c.3. SS administrator chooses to continue with adding the WSDL or REST. Use case continues from step 7.
        - 6c.2a. SS administrator selects to terminate the use case.

- 6d. The address of the WSDL or REST validator program is incorrect and system was not able to run the validation program.
    - 6d.1. System displays the error message “Running WSDL (or REST) validator failed. Command not found.”.
    - 6d.2. System logs the event “Add service description failed” to the audit log.
    - 6b.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 6b.3a. SS administrator selects to terminate the use case.

- 6e. The address of the WSDL or REST validator refers to non-executable file and system was not able to run the validation program.
    - 6e.1. System displays the error message “Running WSDL (or REST) validator failed. Command not executable.”.
    - 6e.2. System logs the event “Add service description failed” to the audit log.
    - 6b.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 6b.3a. SS administrator selects to terminate the use case.

- 7a. A service with the same service code and version values as a service read from the WSDL or REST file was found for this client in the system configuration.
    - 7a.1. System displays the error message "Failed to add WSDL (or REST): Duplicate service. Service 'X' already exists in WSDL or REST 'Y'" (where “X” is the code.version of the service and “Y” is the URL of the existing WSDL where the duplicate service was found).
    - 7a.2. System logs the event “Add service description failed” to the audit log.
    - 7a.3. SS administrator selects to reinsert the URL of the WSDL OE REST. Use case continues from step 3.
        - 7a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The system parameters are described in document “X-Road: System
    Parameters” \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].