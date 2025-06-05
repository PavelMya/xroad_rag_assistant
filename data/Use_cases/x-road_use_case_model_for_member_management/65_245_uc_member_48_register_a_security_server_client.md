#### 2.4.5 UC MEMBER\_48: Register a Security Server Client

**System**: Security server

**Level**: User task

**Component:** Security server, Central server

**Actors**:

-   SS administrator

-   Management services' security server

**Brief Description**: SS administrator initiates the process of registering a security server client. System sends a security server client registration request to the central server.

**Preconditions**:

-   The state of the security server client is *saved*.

-   The security server client is not the owner of the security server.

-   The member that owns the subsystem to be registered as a security server client has a signing key and certificate.

**Postconditions**: An audit log record for the event is created.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to initiate the registration of a security server client.

2.  System verifies that the selected subsystem exists in the global configuration.

3.  System creates an X-Road SOAP request containing the security server client registration request.

4.  System sends the request to the management services' security server: see UC MESS\_02 \[[UC-MESS](#Ref_UC-MESS)\], where this system acts as both the Client IS and the System; the owner of this security server acts as the service client; and the central server acts as the Provider IS.

5.  System receives the response from the management services' security server and verifies that the response was not an error message.

6.  System sets the state of the client to *registration in progress*.

7.  System logs the event “Register client” to the audit log.

**Extensions**:

2a. The subsystem does not exist in the global configuration.

  - 2a.1. System prompts the message “New subsystem 'X' will be submitted for registration for member 'Y'.” (where “X” is the subsystem code and “Y” the member identifier part of the client identifier) and asks for confirmation for continuing.

  - 2a.2. SS administrator selects to continue. Use case continues from step 3.

    - 2a.2a. SS administrator selects not to continue and terminates the use case.

3-5a. The creating or sending of the registration request failed, or the response was an error message.

  - 3-5a.1. System displays the error message: “Failed to send registration request: X”, where “X” is the description of the encountered error.

  - 3-5a.2. System logs the event “Register client failed” to the audit log.

  - 3-5a.3. Use case terminates.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The security server client state machine model is described in the document “Security Server User Guide” \[[UG-SS](#Ref_UG-SS)\].

-   The protocol for sending management requests is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].