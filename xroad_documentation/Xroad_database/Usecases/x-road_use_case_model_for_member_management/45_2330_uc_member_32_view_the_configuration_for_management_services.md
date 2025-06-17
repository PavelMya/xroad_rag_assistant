#### 2.3.30 UC MEMBER\_32: View the Configuration for Management Services

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator view the configuration for management services.

**Preconditions**: -

**Postconditions**: The configuration for management services has been displayed to CS administrator.

**Trigger**: CS administrator needs to configure management services in the management services' security server.

**Main Success Scenario**:

1.  CS administrator selects to view the configuration for management services.

2.  System displays the following information:

    -   the X-Road identifier of the management services provider;

    -   the name of the management services provider;

    -   the X-Road identifiers of the security servers where the management service provider is registered as a security server client;

    -   the URL of the WSDL file describing the management services;

    -   the address of the management services (i.e., the address where the service requests received by the management services' security server should be forwarded);

    -   the code of the global group that needs to have access rights to management services. This group is managed by the central server software and comprises of the owners (X-Road members) of registered security servers.

    The following user action options are displayed:

    -   change the provider of the management services: [2.3.31](#2331-uc-member_33-change-the-management-service-provider);

    -   register the management service provider as a security server client: [2.3.32](#2332-uc-member_57-register-the-management-service-provider-as-a-security-server-client).

**Extensions**: -

**Related information**: -