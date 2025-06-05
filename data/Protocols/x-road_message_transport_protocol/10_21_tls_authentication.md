### 2.1 TLS Authentication

Security servers use authentication certificates to initiate a mutually authenticated message exchange. Each security server's authentication certificate must be registered at the central server. The certification service provider that issued these certificates must be approved by the central server. Therefore, certificate chains constructed when authenticating the connection must include certificates up to the issuing certificate of the trusted certification service provider that is registered at the central server as an approved certification authority.

The process of establishing of a secure communication channel can be described by the following steps.

1. An X-Road request message arrives at the service client's security server.

2. Service client's security server processes the request and determines the target service provider's security server.

3. Service client's security server initiates the TLS handshake with the target service provider's security server on port 5500 (default configuration).

4. Service client's security server receives the authentication certificate chain of the service provider's security server as part of the TLS handshake.

5. Service client's security server checks if the local OCSP cache contains OCSP responses for the received certificates.

6. If the OCSP responses are not cached, the service client's security server must download them from the service provider's security server and cache them locally (see [Section 2.2](#22-downloading-ocsp-responses-from-service-provider) for details).

7. Service client's security server verifies that the authentication certificate of the service provider's security server was issued by an approved certification service provider and builds the certification chain for the authentication certificate. The certification chain and corresponding OCSP responses are then verified.

8. If verification is successful, the service client's security server forwards the X-Road transport message to the service provider's security server. If verification failed, the service client's security server sends a SOAP Fault message back to the service client's information system.

9. Having received the X-Road transport message, the service provider's security server verifies the service client's authentication certificate chain using the global configuration.

This process is illustrated in the sequence diagram in Figure 3.

<a id="Messtransport_protocol_auth" class="anchor"></a>
![](img/pr-messtransport-protocol-auth.png)

Figure 3. TLS authentication