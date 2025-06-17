### 3.43 UC SS\_42: Unregister an Authentication Certificate on Key Deletion

**System**: Security server

**Level**: Subfunction

**Component:** Security server

**Actors**: -

**Brief Description**: System creates and sends an authentication
certificate deletion request to the management services' security
server, waits for the response and sets the state of the authentication
certificate to “deletion in progress”.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 2 of 3.36.

**Main Success Scenario**:

1.  System creates an X-Road SOAP request containing the authentication
    certificate deletion request for the certificate. The contents of
    the request is described in \[[PR-MSERV](#Ref_PR-MSERV)\].

2.  System sends the request to the management services' security
    server: see UC MESS\_02 \[[UC-MESS](#Ref_UC-MESS)\], where this system acts as both
    the Client IS and the System; the owner of this security server acts
    as the service client; and the central server acts as the Provider
    IS.

3.  System receives the response from the management services' security
    server and verifies that the response is not an error message.

4.  System sets the registration status of the authentication
    certificate to “deletion in progress”.

**Extensions**:

- 1-2a. The creating or sending of the deletion request failed.
    - 1-2a.1. Use case terminates with the error message describing the failure.

- 3a. The response was an error message.
    - 3a.1. Use case terminates with the received error message.

**Related information:** -