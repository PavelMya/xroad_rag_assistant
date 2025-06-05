#### 2.3.26 UC MEMBER\_28: Handle an Authentication Certificate Registration Request

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System parses the request and verifies the contents of the request. System saves the request and sets the status of the request.

**Preconditions**: -

**Postconditions**: System has processed the request and either saved the request or created an exception message.

**Trigger**: Step 2 of [2.3.25](#2325-uc-member_27-serve-a-management-service-request).

**Main Success Scenario**:

1.  System parses the authentication certificate registration request message and verifies that all required parts are included in the message.

2.  System verifies the SOAP message contained in the request: see UC MESS\_04 \[[UC-MESS](#Ref_UC-MESS)\].

3.  System verifies the signature that was created using the private key part of the authentication key the authentication certificate was issued for.

4.  System verifies the signature of the security server owner.

5.  System builds the certificate chain from the security server owner's certificate to a trusted certification authority (CA) certificate and verifies the certificate chain: see UC MESS\_07 \[[UC-MESS](#Ref_UC-MESS)\].

6.  System builds the certificate chain from the authentication certificate to a trusted certification authority (CA) certificate and verifies the certificate chain: see UC MESS\_07 \[[UC-MESS](#Ref_UC-MESS)\].

7.  System verifies that the request was sent by a security server of this X-Road instance.

8.  System verifies that the security server owner identifier read from the security server identifier matches the service client identifier from the SOAP message header.

9.  System verifies that the certificate submitted for registration is not already registered for the security server.

10. System verifies that no other authentication certificate registration request have been received for the authentication certificate contained in the request. The previously created requests that are in the *revoked* or *declined* state are not included in this verification.

11. System saves the authentication certificate registration request and sets the status of the request: [2.3.10](#2310-uc-member_13-set-registration-request-status).

**Extensions**:

1a. The parsing process terminated with an error.

  - 1a.1. Use case terminates with the exception message containing the error message from the parsing process.

1b. The SOAP message is missing from the request.

  - 1b.1. Use case terminates with the exception message “Request contains no SOAP message”.

1c. The signature algorithm identifier for the authentication certificate signature is missing.

  - 1c.1. Use case terminates with the exception message “Auth signature algorithm id is missing”.

1d. The signature algorithm identifier for the security server owner's signature is missing.

  - 1d.1. Use case terminates with the exception message “Owner signature algorithm id is missing”.

1e. The authentication certificate signature is missing.

  - 1e.1. Use case terminates with the exception message “Auth signature is missing”.

1f. The security server owner's signature is missing.

  - 1f.1. Use case terminates with the exception message “Owner signature is missing”.

1g. The authentication certificate is missing.

  - 1g.1. Use case terminates with the exception message “Auth certificate is missing”.

1h. The security server owner's certificate is missing.

  - 1h.1. Use case terminates with the exception message “Owner certificate is missing”.

1i. The OCSP response for the owner's certificate is missing.

  - 1i.1. Use case terminates with the exception message “Owner certificate OCSP is missing”.

2a. The process of verifying the SOAP message terminated with an exception message.

  - 1a.1. Use case terminates with the exception message from the SOAP verification process.

3a. The authentication certificate signature verification failed.

  - 3a.1. Use case terminates with the exception message “Auth signature verification failed”.

4a. The security server owner's signature verification failed.

  - 4a.1. Use case terminates with the exception message “Owner signature verification failed”.

5a. The building or verifying the security server owner's certificate chain failed.

  - 5a.1. Use case terminates with the exception message “Owner certificate is invalid: X”, where “X” is the error message from validation process.

6a. The building or verifying the authentication certificate chain failed.

  - 6a.1. Use case terminates with the exception message “Authentication certificate is invalid: X”, where “X” is the error message from validation process.

7a. The instance identifier found in the security server identifier in the management request do not match the instance identifier of this X-Road instance.

  - 7a.1. Use case terminates with the exception message “Invalid management service address. Contact central server administrator”.

8a. The security server owner identifier and the service client identifier do not match.

  - 8a.1. Use case terminates with the exception message “The security server owner identifier in the request (X) and the service client identifier (Y) in the SOAP header do not match”, where “X” is the X-Road identifier read from the *server* element of the SOAP body and “Y” is the X-Road identifier read from the *client* element of the SOAP header.

9a. The submitted certificate is already registered for the security server.

  - 9a.1. Use case terminates with the exception message “Certificate is already registered, request id 'X'”, where X is the identifier of the previous authentication certificate registration request submitted to register the certificate.

10a. A request containing the authentication certificate has already been received.

  - 10a.1. Use case terminates with the exception message “Certificate is already submitted for registration with request 'X'”, where “X” is the identifier of the registration request that contains the certificate.

**Related information**:

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].