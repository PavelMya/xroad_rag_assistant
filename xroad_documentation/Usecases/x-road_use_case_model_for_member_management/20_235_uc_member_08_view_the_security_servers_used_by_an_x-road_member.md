#### 2.3.5 UC MEMBER\_08: View the Security Servers Used by an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of security servers where the X-Road member's subsystems are registered as security server clients.

**Preconditions**: -

**Postconditions**: The list of security servers used by the subsystems of the member have been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the security servers used by an X-Road member.

2.  The system displays the list of security servers that have the member's subsystems registered as security server clients. The following information is displayed for each security server:

    -   the code of the security server;

    -   the code of the subsystem that is the client of the security server;

    -   the name of the owner of the security server.

    The following user action options are displayed:

    -   view the details of the security server that has a subsystem of the member registered as a security server client: [2.3.16](#2316-uc-member_18-view-the-details-of-a-security-server);

    -   view the details of the owner of the security server that has the a subsystem of the member registered as a security server client: [2.3.2](#232-uc-member_05-view-the-details-of-an-x-road-member);

    -   create a security server client registration request for registering a subsystem of the member as a client to a security server: [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request);

    -   create a security server client deletion request to delete the registration of a member's subsystem as a client of a security server: [2.3.14](#2314-uc-member_16-create-a-security-server-client-deletion-request).

**Extensions**: -

**Related information**: -