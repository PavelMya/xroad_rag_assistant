#### 2.3.25 UC MEMBER\_27: Serve a Management Service Request

**System**: Central server

**Level**: System task

**Component:** Central server, security server

**Actor**: Security server

**Brief Description**: System receives and handles a management request form a security server and responds.

**Preconditions**: -

**Postconditions**: The system has responded to the management service request with the identifier of the management request or with an error message.

**Trigger**: Management service request.

**Main Success Scenario**:

1.  System receives a management service request from a security server.

2.  System handles the management request depending of the type of the request:

    -   authentication certificate registration request: [2.3.26](#2326-uc-member_28-handle-an-authentication-certificate-registration-request);

    -   authentication certificate deletion request: [2.3.27](#2327-uc-member_29-handle-an-authentication-certificate-deletion-request);

    -   security server client registration request: [2.3.28](#2328-uc-member_30-handle-a-security-server-client-registration-request);

    -   security server client deletion request: [2.3.29](#2329-uc-member_31-handle-a-security-server-client-deletion-request).

3.  System verifies that the handling process did not terminate with an exception message and creates a response message containing the SOAP message from the management request and the identifier of the saved management request.

4.  System sends the response message to the security server.

**Extensions**:

3a. The handling of the management request terminated with an error message.

  - 3a.1. System creates a response message containing the termination message of the request handling process.

  - 3a.2. Use case continues from step 4.

**Related information**:

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].