#### 2.3.28 UC MEMBER\_30: Handle a Security Server Client Registration Request

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System parses the request and verifies the contents of the request. System saves the request and sets the status of the request.

**Preconditions**: -

**Postconditions**: System has processed the request and either saved the request or created an exception message.

**Trigger**: Step 2 of [2.3.25](#2325-uc-member_27-serve-a-management-service-request).

**Main Success Scenario**:

1.  System parses the security server client registration request.

2.  System verifies that the request was sent by a security server of this X-Road instance to register a subsystem of an X-Road member of this X-Road instance.

3.  System verifies that the security server owner identifier read from the security server identifier matches the service client identifier from the SOAP message header.

4.  System verifies that the client is not already registered as a client of the security server.

5.  System verifies that a duplicate of the request does not exist in the system configuration. The previously received requests that are in the *revoked* or *declined* state are not included in this verification.

6.  System saves the request and sets the status of the request: [2.3.10](#2310-uc-member_13-set-registration-request-status).

**Extensions**:

1a. The parsing process terminated with an error.

  - 1a.1. Use case terminates with the exception message containing the error message from the parsing process.

2a. The instance identifiers found in the security server identifier or security server client identifier in the management request do not match the instance identifier of this X-Road instance.

  - 2a.1. Use case terminates with the exception message “Invalid management service address. Contact central server administrator”.

3a. The security server owner identifier and the service client identifier do not match.

  - 3a.1. Use case terminates with the exception message “The security server owner identifier in the request (X) and the service client identifier (Y) in the SOAP header do not match”, where “X” is the X-Road identifier read from the *server* element of the SOAP body and “Y” is the X-Road identifier read from the *client* element of the SOAP header.

4a. The registration relation requested by the registration request already exists.

  - 4a.1. Use case terminates with the exception message “'X' has already been registered as a client to security server 'Y'”, where “X” is the X-Road identifier of the client and “Y” is the X-Road identifier of the security server.

5a. A duplicate request is found.

  - 5a.1. Use case terminates with the exception message “Failed to add new server client request: A request for registering 'X', as a client to security server 'Y' has already been submitted (Z, request ID: 'ZZ')'”, where

    -   “X” is the X-Road identifier of the client,

    -   “Y” is the X-Road identifier of the security server,

    -   “Z” is the date and time of when the existing request was saved to the system configuration and

    -   “ZZ” is the identifier of the existing request.

**Related information**:

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].