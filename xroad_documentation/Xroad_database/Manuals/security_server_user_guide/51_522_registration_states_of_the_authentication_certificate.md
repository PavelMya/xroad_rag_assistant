#### 5.2.2 Registration States of the Authentication Certificate

A Security Server authentication certificate can be in one of the following registration states.

**Saved** – the certificate has been imported to the Security Server and saved to its configuration, but the certificate has not been submitted for registration. From this state, the certificate can move to the following states:

-   "Registration in progress", if the authentication certificate registration request is sent from the Security Server to the Central Server (see [3.3.1](#331-registering-an-authentication-certificate));

-   "Deleted", if the authentication certificate's information is deleted from the Security Server configuration (see Section [5.6](#56-deleting-a-certificate)). Notice that after the certificate is deleted, it will not be displayed in the table anymore.

**Registration in progress** – an authentication certificate registration request has been created and sent to the Central Server, but the association between the certificate and the Security Server has not yet been approved. From this state, the certificate can move to the following states:

-   "Registered", if the association between the authentication certificate and the Security Server is approved by the X-Road governing authority (see [3.3](#33-registering-the-security-server-in-the-x-road-governing-authority));

-   "Deletion in progress", if the certificate deletion request has been submitted to the Central Server (see [5.6.1](#561-unregistering-an-authentication-certificate)). The user can force this state transition even if the sending of the authentication certificate deletion request fails.

**Registered** – the association between the authentication certificate and the Security Server has been approved in the Central Server. An authentication certificate in this state can be used to establish a secure data exchange channel for exchanging X-Road messages. From this state, the certificate can move to the following states:

-   "Global error", if the association between the authentication certificate and the Security Server has been revoked in the Central Server;

-   "Deletion in progress", if the certificate deletion request has been transmitted to the Central Server (see [5.6.1](#561-unregistering-an-authentication-certificate)). The user can force this state transition even if the sending of the authentication certificate deletion request fails.

**Global error** – the association between the authentication certificate and the Security Server has been revoked in the Central Server. From this state, the certificate can move to the following states:

-   "Registered", if the association between the authentication certificate and the Security Server has been restored in the Central Server (e.g., the association between the client and the Security Server was lost due to an error);

-   "Deleted", if the authentication certificate's information is deleted from the Security Server configuration (see [5.6](#56-deleting-a-certificate)). Notice that after the certificate is deleted, it will not be displayed in the table anymore.

**Deletion in progress** – an authentication certificate registration request has been created for the certificate and sent to the Central Server. From this state, the certificate can be deleted. If the certificate has been deleted from the Security Server configuration, it will not be displayed in the table anymore.