#### 4.6.2 Deleting a Client

**Access rights:** [Registration Officer](#xroad-registration-officer)

A Security Server client can be deleted if its state is "Saved", "Global error" or "Deletion in progress". Clients that are in states "Registered" or "Registration in progress" need to be unregistered before they can be deleted (see Section [4.6.1](#461-unregistering-a-client)).

To delete a client, follow these steps.

1.  In the **CLIENTS** view click the name of the client you wish to remove from the Security Server.

2.  In the window that opens, click **DELETE** and then click **YES**. If there are no users for the signature key nor for the certificate associated then an option is presented to delete the client's certificates. To delete the certificates, click **YES** again.