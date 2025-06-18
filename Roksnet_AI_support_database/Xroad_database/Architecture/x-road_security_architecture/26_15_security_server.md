## 15 Security Server

The main function of a Security Server is to mediate requests in a way that preserves their evidential value. The Security Server is connected to the public Internet from one side and to the information system within the organization's internal network from the other side (refer to Figure 1 X-Road Security Architecture). The Security Server is equipped with the functionality required to secure the message exchange between a client and a service provider.

A Security Server instance is an independent and separately identifiable entity. A Security Server identity consist of a server identifier (member id + server code). For each server identifier there may be multiple authentication certificates present locally, each of which must be unique. However, only one authentication certificate must be active and registered on the Central Server at a time. In addition, each Security Server has an address (DNS name or IP address) which is not required to be unique. The global configuration binds together the authentication certificate(s), server identifier and address. The authentication certificate may contain information about the service identifier; however this is optional. Also, the server address and the common name or alternate subject names in the authentication certificate may be different.

Messages transmitted over the public Internet are secured using digital signatures and TLS (HTTPS) encryption. On every connection, the Security Server verifies that the authentication certificate of the other Security Server:

  * is issued by an approved certification authority
  * matches the authentication certificate registered to the Security Server on the global configuration
  * has a valid OCSP response available.
  
If any of the above verifications fail, the message is not processed further and an error message is returned.

The service provider's Security Server applies access control to incoming messages, thus ensuring that only those X-Road members (consumer information systems) that have been explicitly allowed access can access a service. Managing access rights of a service is the responsibility of the administrator of the service provider's Security Server.

For Security Server components, refer to \[[ARC-SS](#Ref_ARC-SS)\] section 2.

For Security Server roles, refer to \[[UG-SS](#Ref_UG-SS)\] section 2.