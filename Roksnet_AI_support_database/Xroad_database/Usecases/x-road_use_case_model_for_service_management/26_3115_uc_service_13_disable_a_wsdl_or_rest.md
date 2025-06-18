#### 3.1.15 UC SERVICE\_13: Disable a WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator disables a WSDL or REST. The
services included in the WSDL or REST will not be available for service clients.
Clients who request to use these services will get the notice message
inserted by SS administrator as a response.

**Preconditions**: The WSDL or REST is not disabled.

**Postconditions**: -

**Trigger**: SS administrator wants make the services described in the
WSDL unavailable for the service clients.

**Main** **Success** **Scenario**:

1.  SS administrator selects to disable a WSDL or REST.

2.  System asks for notice message that will be sent as a response to
    service clients trying to access services described in the WSDL or REST.

3.  SS administrator inserts the message.

4.  System parses user input: 3.1.13.

5.  System disables the services described in the WSDL or REST. Service clients
    trying to access the disabled services will get the following error
    message as response: “Service X is disabled: Y”, where “X” is the
    X-Road identifier of the service and “Y” is the inserted notice
    message.

6.  System logs the event “Disable service description” to the audit log.

**Extensions**:

- 3a. SS administrator terminates the use case.

- 4a. The process of parsing the user input terminated with an error message.
    - 4a.1. System displays the error message “X” (where “X” is the termination message from the parsing process).
    - 4a.2. System logs the event “Disable service description failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the message. Use case continues from step 4.
        - 4a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].