#### 2.4.1 UC MEMBER\_44: View Security Server Clients

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator views the clients of the security server.

**Preconditions**: -

**Postconditions**: The list of clients of the security server and their structure Member (Owner), Members and their Subsystems has been displayed to SS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to view the security server clients.

2.  System displays the list structure of clients Member (Owner), Members and related Subsystems. The following information is displayed for each client in the view.

    -   The name of the client. A clear structured list defines with the help of icons the hierarchy of the clients. The Name of the client opens a view of the details of the desired client. Note: SS administrators can not view details of the members not owned by the Security Server.
    
    -   The X-Road identifier of the Member (Owner) and all Subsystems ("Member or Subsystem":"Instance":"Member Class":"Server code":"Client name")
    
    -   The status of the Member (Owner) and all Subsystems 
    
    -   The option to add a Subsystem (in case a client is a member)

    The following user action options are displayed:
    
    -   Search for a Client

    -   Add a client: [2.4.4](#244-uc-member_47-add-a-client-to-the-security-server);
    
    -   Add a subsystem (in case a member is already available in the Security Server)

    -   View the details of a client (via Client's name)

**Extensions**: -

**Related information**:

-   The security server client state machine model is described in the document “Security Server User Guide” \[[UG-SS](#Ref_UG-SS)\].