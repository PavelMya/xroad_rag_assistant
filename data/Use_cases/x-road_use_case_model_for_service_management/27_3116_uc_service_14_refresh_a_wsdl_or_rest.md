#### 3.1.16 UC SERVICE\_14: Refresh a WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator refreshes a WSDL or REST. System
reloads the WSDL file from the WSDL or REST address.

**Preconditions**: -

**Postconditions**: -

**Trigger**:

-   SS administrator wants to refresh a WSDL or REST.

-   Step 5 of 3.1.10.

**Main** **Success** **Scenario**:

1.  SS administrator selects to refresh the WSDL or REST.

2.  System downloads the WSDL file from the WSDL or REST URL and reads service
    information from the downloaded file: 3.1.11.

3.  System verifies that the location of a WSDL or REST validation program is
    described by the system parameter *wsdl-validator-command* or *rest-validator-command* and
    validates the WSDL or REST file using the validator: 3.1.12.

4.  System verifies that none of the services described for this
    security server client in other WSDLs or RESTs than the one being refreshed
    have the same service code and service version value combination as
    any of the services read from the downloaded WSDL or REST file.

5.  System verifies that the composition of the services in the
    downloaded WSDL or REST does not differ from the current version.

6.  System updates the list of services saved in the system
    configuration for this WSDL or REST.

7.  System logs the event “Refresh service description” to the audit log.

**Extensions**:

- 2a. The process of downloading and parsing the WSDL or REST file terminated with an error message.
    - 2a.1. System displays the error message “X” (where “X” is the termination message from the downloading and parsing process).
    - 2a.2. System logs the event “Refresh service description failed” to the audit log.
        - 2a.2a. The process of refreshing the WSDL or REST was triggered from the use case 3.1.10. Use case terminates.
    - 2a.3. Use case terminates.

- 3a. The location of the WSDL or REST validator is not set.
    - 3a.1. System skips the process of validation.
    - 3a.2. Use case continues from step 4.

- 3b. The process of validating the WSDL or REST file was terminated with an error message.
    - 3b.1. System displays WSDL or REST validator output describing the reason of the failure, and the error message from the validation process.
    - 3b.2. System logs the event “Refresh service description failed” to the audit log.
        - 3b.2a. The process of refreshing the WSDL or REST was triggered from the use case 3.1.10 . Use case terminates.
    - 3b.3. Use case terminates.

- 3c. The process of validating the WSDL or REST file was finished with a warning message.
    - 3c.1. System prompts the warning message “WSDL (or REST) ('X') validation gave the following warnings: 'Y'. Do you want to continue?” (where “X” is the URL of the WSDL or REST and “Y” is the message from the validation process).
    - 3c.2. SS administrator chooses to continue with the refreshing process. Use case continues from step 4.
        - 3c.2a. SS administrator selects to terminate the use case.

- 3d. The address of the WSDL or REST validator program is incorrect and system was not able to run the validation program.
    - 3d.1. System displays the error message “Running WSDL (or REST) validator failed. Command not found.”.
    - 3d.2. System logs the event “Refresh service description failed” to the audit log.
        - 3d.2a. The process of refreshing the WSDL or REST was triggered from the use case 3.1.10. Use case terminates.
    - 3d.3. Use case terminates.

- 3e. The address of the WSDL or REST validator refers to non-executable file and system was not able to run the validation program.
    - 3e.1. System displays the error message “Running WSDL (or REST) validator failed. Command not executable.”.
    - 3e.2. System logs the event “Refresh service description failed” to the audit log.
        - 3e.2a. The process of refreshing the WSDL or REST was triggered from the use case 3.1.10 . Use case terminates.
    - 3e.3. Use case terminates.

- 4a. A service with the same service code and version values as a service read from the WSDL or REST file is described in another WSDL or REST of the service client.
    - 4a.1. System displays the error message “Duplicate service. Service 'X' already exists in WSDL or REST 'Y'” (where “X” is the code.version of the service and “Y” is the URL of the existing WSDL or REST where the duplicate service was found).
    - 4a.2. System logs the event “Refresh service description failed” to the audit log.
        - 4a.2a. The process of refreshing the WSDL or REST was triggered from the use case 3.1.10. Use case terminates.
    - 4a.3. Use case terminates.

- 5a. The composition of the services in the downloaded WSDL or REST differ from the current version.
    - 5a.1. System prompts the warning “Adding services: 'X' Deleting services: 'Y'” (where “X” and “Y” is the list of the service codes that have been added to or removed from the WSDL or REST) and asks for confirmation to continue.
    - 5a.2. System logs the event “Adding service description failed” to the audit log.
    - 5a.3. SS administrator selects to continue with the refreshing process. Use case continues from step 6.
        - 5a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The system parameters are described in document “X-Road: System
    Parameters” \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].