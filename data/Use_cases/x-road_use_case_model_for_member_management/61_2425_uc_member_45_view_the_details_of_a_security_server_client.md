#### 2.4.25 UC MEMBER\_45: View the Details of a security Server client

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator views the details of a Security Server client.

**Preconditions**: -

**Postconditions**: The details of the Security Server client have been displayed to SS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to view the details the Security Server client.

2.  System displays the following information.

    -   The name of the X-Road Security Server client.

    -   The member class, member code and subsystem code of the security server client.

    Depending on the status of the client, the following user action options are displayed:

    -   start the registration process for the security server client by sending a security server client registration request to the central server: [2.4.5](#245-uc-member_48-register-a-security-server-client);

    -   unregister the client from the security server by sending a security server client deletion request to the central server: [2.4.9](#249-uc-member_52-unregister-a-security-server-client);

    -   delete the security server client: [2.4.10](#2410-uc-member_53-delete-a-security-server-client);

**Extensions**: -

**Related information**: -