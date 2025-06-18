#### 2.1.2 UC MEMBER\_02: Configure and Register a Subsystem of the Security Server Owner as a Security Server Client

**System**: X-Road system

**Level**: Summary

**Component:** Central server, Security server

**Actors**:

-   CS administrator – the administrator of the central server of the local X-Road instance.

-   SS administrator – the administrator of the security server owned by the X-Road member who wishes to register it's subsystem as a security server client.

**Brief Description**: SS administrator adds the subsystem as a security server client and initiates the registration of the subsystem. CS administrator completes the registration of the subsystem as the client of the security server. SS administrator configures the subsystem for using and/or providing services.

**Preconditions**: The use case assumes that the security server is configured and registered: [2.1.1](#211-uc-member_01-configure-and-register-a-security-server).

**Postconditions**: A subsystem of the security server owner is registered as the security server client and ready to use and/or provide X-Road services.

**Trigger**: The security server owner wishes to use the security server to use or provide X-Road services.

**Main Success Scenario**:

1.  SS administrator adds a subsystem of the security server owner as a client of the security server: [2.4.4](#244-uc-member_47-add-a-client-to-the-security-server).

2.  SS administrator initiates the registration of the subsystem:

    -   sends a security server client request from the security server: [2.4.5](#245-uc-member_48-register-a-security-server-client) (the request is served by the central server: [2.3.25](#2325-uc-member_27-serve-a-management-service-request)) and

    -   sends a security server client request to the X-Road governing authority via out-of-band means.

3.  CS administrator completes the registration of the subsystem:

    -   creates a security server client registration request: [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request) and

    -   approves the registration requests: [2.3.36](#2336-uc-member_37-approve-a-security-server-client-registration-request).

    -   The central server generates and distributes global configuration that contains the created registration relation between the security server and the subsystem: UC GCONF\_18 \[[UC-GCONF](#Ref_UC-GCONF)\].

4.  SS administrator waits for the security server to update configuration: UC GCONF\_23 \[[UC-GCONF](#Ref_UC-GCONF)\] and verifies that the state of the subsystem is *registered*: [2.4.1](#241-uc-member_44-view-security-server-clients).

5.  In case the subsystem is used in the service client role, SS administrator configures the settings for internal server communication: [2.4.6](#246-uc-member_49-change-a-security-server-clients-internal-server-connection-type), and adds internal TLS certificates to the subsystem if HTTPS connection is used: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate).

6.  In case the subsystem is used in the service provider role, SS administrator:

    -   adds internal TLS certificates to the subsystem if HTTPS connection is used to communicate with the internal servers: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate) and

    -   configures the services and access rights: \[[UC-SERVICE](#Ref_UC-SERVICE)\].

**Extensions**: -

**Related information**: -