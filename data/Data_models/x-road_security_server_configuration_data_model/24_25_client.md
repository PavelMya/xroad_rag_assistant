### 2.5 CLIENT

Member or subsystem that is using this security server. The security server owner is also registered as a client.
For owner, the record is created when the administrator initializes the security server. For security server users, the record is created when the administrator adds new client in the user interface.
The client record is deleted when the administrator removes the client in the user interface. The client record corresponding to the owner cannot be deleted.
The client record is modified when administrator changes parameters in the user interface or when automatic status update occurs (see below).
The field clientstatus shows the progress of registering in central server the connection between this security server client and this security server. Only in “registered” state can the security server exchange messages on behalf of this client.

* _saved_ -- initial state. Client enters it immediately after creation. From this state the administrator can send registration request to the central server.
* _registration in progress_ -- the administrator has successfully sent registration request to the central server. In this state the security server is waiting for approval of the client registration request. When the security server receives a global configuration that contains connection between the security server and the client, it enters the “registered” state.
* _registered_ -- the registration request sent to the central server is approved and the connection between the client and the security server is registered in the global configuration. In this state the security server can exchange messages on behalf of the client.
* _deletion in progress_ -- the security server has successfully sent client deletion request to the central server. From this state, the only possible action is to delete the client from security server configuration.
* _global error_ -- the client was in state “registered”, but the connection between the client and the security server has been deleted from the global configuration. From this state the administrator can either wait for updated global configuration (in case the deletion was caused by an error), contact the systems administrator of the central server or delete the client.
* _disabled_ -- the client is temporarily disabled
* _disabling in progress__ -- the administrator has successfully sent clientDisable request. When the security server receives updated global configuration, it enters the "disabled" state. 
* _enabling in progress__ -- the administrator has successfully sent clientEnable request. When the security server receives updated global configuration, it returns to "registered" state.