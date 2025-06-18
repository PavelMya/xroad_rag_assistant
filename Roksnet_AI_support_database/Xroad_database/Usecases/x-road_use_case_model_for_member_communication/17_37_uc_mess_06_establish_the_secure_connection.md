### 3.7 UC MESS\_06: Establish the Secure Connection

**System**: Service provider's security server

**Level**: Subfunction

**Component**: Security server

**Actor**: Client SS

**Brief Description**: The system finishes setting up the secure connection initiated by the Client SS by validating the authentication information received from the Client SS.

**Preconditions**: Client SS has initiated the secure connection and the system has received validation information from the Client SS.

**Postconditions**: -

**Trigger**: Step 5 of [3.4](#34-uc-mess_03-process-x-road-request-message).

**Main Success Scenario**:

1.  System verifies that the request message received from the Client SS contains OCSP responses.

2.  System verifies that the authentication certificate of the Client SS was issued by an approved certification service provider.

3.  System verifies the authentication certificate of the Client SS: [3.8](#38-uc-mess_07-verify-authentication-certificate).

**Extensions**:

1a. System cannot find the OCSP response needed to verify the authentication certificate.

  - 1a.1. System creates an exception message: “Cannot verify TLS certificate, corresponding OCSP response is missing“. The use case terminates.

2a. The authentication certificate issuer is not listed as an approved certification service in the global configuration.

  - 2a.1. System creates an exception message: “Certificate is not issued by approved certification service provider“. The use case terminates.

3a. The verification process terminates with an exception message.

  - 3a.1. The use case terminates with the exception message.

**Related information**: -