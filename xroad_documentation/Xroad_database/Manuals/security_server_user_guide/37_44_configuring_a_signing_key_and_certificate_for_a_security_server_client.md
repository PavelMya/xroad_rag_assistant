### 4.4 Configuring a Signing Key and Certificate for a Security Server Client

A signing key and certificate must be configured for the Security Server client to sign messages exchanged over the X-Road. In addition, a signing key and certificate are required for registering a Security Server client.

Certificates are not issued to subsystems; therefore, the certificate of the subsystem's owner (that is, an X-Road member) is used for the subsystem.

All particular X-Road member's subsystems that are registered in the same Security Server use the same signing certificate for signing messages. Hence, if the Security Server already contains the member's signing certificate, it is not necessary to configure a new signing key and/or certificate when adding a subsystem of that member.

The process of configuring the signing key and certificate for a Security Server client is the same as for the Security Server owner. The process is described in Section [3.1](#31-configuring-the-signing-key-and-certificate-for-the-security-server-owner).