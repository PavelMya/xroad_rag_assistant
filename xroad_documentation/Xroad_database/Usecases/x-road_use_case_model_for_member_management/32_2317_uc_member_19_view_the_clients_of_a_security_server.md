#### 2.3.17 UC MEMBER\_19: View the Clients of a Security Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of clients registered to a security server, excluding the security server owner.

**Preconditions**: -

**Postconditions**: The list of clients registered to the security server has been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the clients of a security server.

2.  System displays the list of clients registered to the security server, excluding the security server owner. The following information is displayed for each client:

    -   the name of the client;

    -   the member class of the client;

    -   the member code of the client;

    -   the subsystem code of the client.

    The following user action options are displayed:

    -   view the details of a client registered to the security server: [2.3.2](#232-uc-member_05-view-the-details-of-an-x-road-member);

    -   add a client to the security server: [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request);

    -   remove a client from the security server: [2.3.14](#2314-uc-member_16-create-a-security-server-client-deletion-request).

**Extensions**: -

**Related information**: -