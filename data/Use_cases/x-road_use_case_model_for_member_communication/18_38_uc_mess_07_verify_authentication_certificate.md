### 3.8 UC MESS\_07: Verify Authentication Certificate

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: The system validates the authentication certificate and verifies that the peer security server is entitled to use the authentication certificate it presented and that it is entitled to send messages on behalf of the service client (in case the Provider SS performs the verification) or the service provider (in case the Client SS performs the verification).

**Preconditions**: -

**Postconditions**: The validity of the authentication certificate is either verified or refuted.

**Triggers**:

-   Step 7 of [3.6](#36-uc-mess_05-initiate-a-secure-connection).

-   Step 3 of [3.7](#37-uc-mess_06-establish-the-secure-connection).

**Main Success Scenario**:

1.  System verifies that the certificate is an authentication certificate (The certificate is an authentication certificate, if it has *ExtendedKeyUsage* extension which contains *ClientAuthentication* or if it has *keyUsage* extension which has *digitalSignature*, *keyEncipherment* or *dataEncipherment* bit set).

2.  System builds the certificate chain from the authentication certificate to a trusted certification authority (CA) certificate.

3.  System verifies the certificate chain: [3.13](#313-uc-mess_12-verify-certificate-chain).

4.  System verifies (using global configuration) that the authentication certificate is registered for the security server who provided the authentication certificate and the security server is entitled to send messages on behalf of the service client/service provider (the service provider/service client is registered as a client of the security server).

**Extensions**:

1a. The certificate is not an authentication certificate.

  - 1a.1. System creates an exception message: “Peer certificate is not an authentication certificate“. The use case terminates.

2a. System does not find enough certificates to build a certificate chain.

  - 2a.1. System creates an exception message: “Chain must have at least user's certificate and root certificate authority“. The use case terminates.

2b. System encounters an error while building the certificate path from the signature certificate to the trusted root certificate.

  - 2b.1. System creates an exception message containing the details of the encountered error. The use case terminates.

3a. The certificate chain validation process terminates with an exception message.

  - 3a.1. The use case terminates with the exception message.

4a. Security server is not entitled to send messages on behalf of the service client/service provider.

  - 4a.1. System creates an exception message: “Client 'X' is not registered at security server Y” (where “X” is the identifier of the service client or service provider and “Y” is the identifier of the security server who provided the authentication certificate). The use case terminates.

4b. The presented authentication certificate is not registered in the central server.

  - 4b.1. System creates an exception message: “Authentication certificate X is not associated with any security server” (where “X” is the subject name of the authentication certificate). The use case terminates.

**Related information**: -