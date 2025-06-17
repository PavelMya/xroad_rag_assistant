### 4.6 Deleting a Client from the Security Server

If a client is deleted from the Security Server, all the information related to the client is deleted from the server as well – that is, the WSDLs, services, access rights, and, if necessary, the certificates.

When one of the clients is deleted, it is not advisable to delete the signing certificate if the certificate is used by other clients registered to the Security Server, e.g., other subsystems belonging the same X-Road member as the deleted subsystem.

A client registered or submitted for registration in the X-Road governing authority (indicated by the "Registered", "Registration in progress" or "Disabled" state) must be unregistered before it can be deleted. The unregistering event sends a Security Server client deletion request from the Security Server to the Central Server.