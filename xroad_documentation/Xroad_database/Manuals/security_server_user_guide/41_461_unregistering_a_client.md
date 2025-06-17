#### 4.6.1 Unregistering a Client

**Access rights:** [Registration Officer](#xroad-registration-officer)

To unregister a client, follow these steps.

1.  In the **CLIENTS** view click the name of client that you wish to remove from the server

2.  In the window that opens, click **UNREGISTER** and then click **YES**. The Security Server automatically sends a client deletion request to the X-Road Central Server, upon the receipt of which the association between the Security Server and the client is revoked.

3.  Next, a notification is displayed about unregistering client. Now the client is moved to the "Deletion in progress" state, wherein the client cannot mediate messages and cannot be registered again in the X-Road governing authority.

**Note:** It is possible to unregister a registered client from the Central Server without sending a deletion request through the Security Server. In this case, the Security Server's administrator responsible for the client must transmit a request containing information about the client to be unregistered to the Central Server's administrator. If the client has been deleted from the Central Server without a prior deletion request from the Security Server, the client is shown in the "Global error" state in the Security Server.