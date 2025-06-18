### 2.5 Certification Authority

The certification authority (CA) issues certificates to security servers (authentication certificates) and to X-Road member organizations (signing certificates). All the certificates are stored in the security servers. The CA must be able to process certificate signing requests conforming to \[[PKCS10](#Ref_PKCS10)\].

The CA must distribute certificate validity information via the OCSP protocol (see Section [3.7](#37-ocsp-protocol)). The security servers cache the OCSP responses to reduce the load in the OCSP service and to increase availability. The load on the OCSP service depends on the number of certificates issued.