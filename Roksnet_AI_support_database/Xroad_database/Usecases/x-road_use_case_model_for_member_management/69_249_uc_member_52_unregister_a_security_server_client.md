#### 2.4.9 UC MEMBER\_52: Unregister a Security Server Client

**System**: Security server

**Level**: User task

**Component:** Security server, Central server

**Actors**:

-   SS administrator

-   Management services' security server

**Brief Description**: SS administrator initiates the process of unregistering a security server client. System sends a security server client deletion request to the central server.

**Preconditions**:

-   The state of the security server client is *registered* or *registration in progress*.

-   The security server client is not the owner of the security server.

**Postconditions**: -

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to unregister a security server client.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System creates an X-Road SOAP request containing the security server client deletion request.

5.  System sends the request to the management services' security server: see UC MESS\_02 \[[UC-MESS](#Ref_UC-MESS)\], where this system acts as both the Client IS and the System; the owner of this security server acts as the service client; and the central server acts as the Provider IS.

6.  System verifies that the response was not an error message.

7.  System sets the state of the client to *deletion in progress*.

8.  System logs the event “Unregister client” to the audit log.

**Extensions**:

3a. SS administrator decides not to unregister the client and terminates the use case.

4-6a. The creating or sending of the deletion request failed, or the response was an error message.

  - 4-6a.1. System displays the error message: “Failed to send deletion request: X”, where “X” is the description of the encountered error.

  - 4-6a.2. System logs the event “Unregister client failed” to the audit log.

  - 4-6a.3. Use case terminates.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The security server client state machine model is described in the document “Security Server User Guide” \[[UG-SS](#Ref_UG-SS)\].

-   The protocol for sending management requests is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].