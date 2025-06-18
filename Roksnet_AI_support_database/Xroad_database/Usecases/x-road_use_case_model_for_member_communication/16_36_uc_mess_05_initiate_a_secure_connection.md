### 3.6 UC MESS\_05: Initiate a Secure Connection

**System**: Service client's security server

**Level**: Subfunction

**Component**: Security server

**Actor**: Provider SS

**Brief Description**: The system initiates a secure connection with the Provider SS and validates the authentication information of the Provider SS.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 11 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

**Main Success Scenario**:

1.  System initiates a TLS handshake with the Provider SS.

2.  System exchanges session authentication information with the Provider SS.

3.  System gets the service provider identifier and authentication certificate from the session authentication information.

4.  System verifies that the authentication certificate was issued by an approved certification service provider and builds the certificate chain from the authentication certificate to a trusted certification authority (CA) certificate.

5.  System finds that one or more of the OCSP responses needed to verify the certificate chain are not cached in the system (from a previous session). System uses the authentication certificate and the registered link between the authentication certificate and the Provider SS to find the address of the Provider SS from the global configuration. System sends a request for missing OCSP responses to the Provider SS.

6.  System receives and caches the OCSP responses.

7.  System verifies the authentication certificate: [3.8](#38-uc-mess_07-verify-authentication-certificate).

8.  System caches the session information.

**Extensions**:

3a. System cannot find usable certificates from the session authentication information.

  - 3a.1. System creates an exception message: “Service provider did not send correct authentication certificate“. The use case terminates.

3b. System cannot find certificates from the session authentication information.

  - 3b.1. System creates an exception message: “Could not get peer certificates from context“. The use case terminates.

4a. The authentication certificate issuer is not listed as an approved certification service in the global configuration.

  - 4a.1. System creates an exception message: “Certificate is not issued by approved certification service provider“. The use case terminates.

5a. System cannot find a link between the Provider SS and the authentication certificate received from the Provider SS from the global configuration (the authentication certificate is not registered in the X-Road central server as a certificate used by the Provider SS).

  - 5a.1. System creates an exception message: “Unable to find provider address for authentication certificate X (service provider: Y)” (where “X” is the serial number of the authentication certificate the Provider SS sent and “Y” is the service provider's identifier). The use case terminates.

6a. System did not receive all the OCSP responses needed to verify the certificate chain.

  - 6a.1. System creates an exception message: “Could not get all OCSP responses from server (expected X, but got Y)” (where “X” is the number of certificates in the certificate chain and “Y” is the number of OCSP responses received from the Provider SS). The use case terminates.

7a. The authentication certificate verification process terminates with an exception message.

  - 7a.1. The use case terminates with the exception message.

**Related information**: -