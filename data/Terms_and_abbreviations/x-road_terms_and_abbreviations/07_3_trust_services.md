## 3 Trust services

**Approved certification service provider** – Provider of a trust service approved on X-Road, who provides at least following trust services approved on X-Road: service of authentication certificate of security server, service of signature certificate of a member, and certificate validation service (OCSP).

**Approved timestamp service provider** – Provider of a trust service approved on X-Road, who provides the timestamp service.

**Authentication certificate of security server** – qualified certificate of e-stamp issued by certification service provider approved on X-Road and bound to security server, certifying authenticity of security server and used for authentication of security servers upon establishment of connection between security servers. Upon establishment of connection, it is checked from global configuration, if the security server trying to establish connection has registered the used authentication certificate in X-Road governing authority (i.e. the used authentication certificate is bound to the ID of security server).

**Certification authority** (**CA**) – is an entity that issues digital certificates. A digital certificate certifies the ownership of a public key by the named subject of the certificate.

**Certification service CA** – is used in the X-Road system as a trust anchor for a certification service. The certification service CA may, but does not have to be a Root CA.

**Certificate signing request**  (**CSR**) – is generated in the security server for a certain approved certification authority for signing a public key and associated information.

**Internal TLS certificates** – are used for setting up the TLS connection between the security server and the client information systems.

**Signature certificate of a member** – qualified certificate of e-stamp issued by certification service provider approved on X-Road and bound to a member, used for verification of the integrity of mediated messages and association of the member with the message.

**Timestamp** – means data in electronic form which binds other data in electronic form to a particular time establishing evidence that the latter data existed at that time (EU No 910/2014)

**Timestamping authority** (**TSA**) – is an entity that issues timestamps. Timestamps are used to prove the existence of certain data before a certain point of time without the possibility that the owner can backdate the timestamps.

**TLS certificate** – is a certificate used by the security server to authenticate the information system when HTTPS protocol is used for connections between the service client's or service provider's security server and information system.

**Validation service** (**OCSP**) – Validation service of the validity of certificate issued by certification service provider approved on X-Road.