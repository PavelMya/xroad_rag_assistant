#### 4.5.1 Registering a Security Server Client

**Access rights:** [Registration Officer](#xroad-registration-officer)

To submit a client registration request follow these steps.

1.  In the **CLIENTS** view.

2.  Click **Register** button on the row that contains the client you wish to register.

3.  Click **YES** to submit the request.

On submitting the request, the message "Request sent" is displayed, and the client's state is set to "Registration in process".

After the X-Road governing authority has accepted the registration, the state of the client is set to "Registered" and the registration process is completed.

**Note:** If the registration request is rejected by the X-Road governing authority, no automatic notification is sent to the Security Server administrator and the client remains in the "Registration in process" state on the Security Server. The X-Road governing authority must notify the Security Server administrator about the rejection of the request through an external channel, e.g., email.

After a rejected client registration request, complete the following steps to send a new client registration request:

1.  Unregister the client (see [4.6.1](#461-unregistering-a-client)).
2.  Delete the client (see [4.6.2](#462-deleting-a-client)).
3.  Add a client (see [4.2](#42-adding-a-security-server-client)) or a subsystem (see [4.3](#43-adding-a-security-server-member-subsystem)).
4.  Register the client (see [4.5.1](#451-registering-a-security-server-client)).