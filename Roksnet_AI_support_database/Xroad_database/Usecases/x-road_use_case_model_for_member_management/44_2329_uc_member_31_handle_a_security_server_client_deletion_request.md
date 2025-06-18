#### 2.3.29 UC MEMBER\_31: Handle a Security Server Client Deletion Request

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System parses the request and verifies the contents of the request. System revokes the registration request or deletes the relation requested by the deletion request.

**Preconditions**: -

**Postconditions**: System has processed the request and either saved the request and executed the action requested by the request or created an exception message.

**Trigger**: Step 2 of [2.3.25](#2325-uc-member_27-serve-a-management-service-request).

**Main Success Scenario**:

1.  System parses the security server client deletion request.

2.  System verifies that the request was sent by a security server of this X-Road instance to unregister a subsystem of an X-Road member of this X-Road instance.

3.  System verifies that the security server owner identifier read from the security server identifier matches the service client identifier from the SOAP message header.

4.  System verifies that the security server specified in the request exists.

5.  System saves the deletion request.

6.  System verifies that the security server client contained in the request has been previously submitted for registration with a registration request sent from the security server and the status of the registration request is *waiting*.

7.  System sets the registration request status to *revoked* and adds the identifier of the deletion request to the registration request.

8.  System verifies that the security server client contained in the request is registered for the security server and deletes the registration relation between the security server and the client.

**Extensions**:

1a. The parsing process terminated with an error.

  - 1a.1. Use case terminates with the exception message containing the error message from the parsing process.

2a. The instance identifiers found in the security server identifier or security server client identifier in the management request do not match the instance identifier of this X-Road instance.

  - 2a.1. Use case terminates with the exception message “Invalid management service address. Contact central server administrator”.

3a. The security server owner identifier and the service client identifier do not match.

  - 3a.1. Use case terminates with the exception message “The security server owner identifier in the request (X) and the service client identifier (Y) in the SOAP header do not match”, where “X” is the X-Road identifier read from the *server* element of the SOAP body and “Y” is the X-Road identifier read from the *client* element of the SOAP header.

4a. The security server with the identifier specified in the request is or registered in the central server.

  - 4a.1. Use case terminates with the exception message “Server not found: X” where X is the X-Road identifier of the security server specified in the request.

6a. System does not find any registration requests in *waiting* status for this security server that contain the security server client.

  - 6a.1. Use case continues from step 8.

8a. The security server client contained in the request is not registered for the security server.

  - 8a.1. Use case terminates.

**Related information**:

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].