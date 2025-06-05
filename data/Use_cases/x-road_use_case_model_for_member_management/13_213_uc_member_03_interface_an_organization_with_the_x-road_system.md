#### 2.1.3 UC MEMBER\_03: Interface an Organization with the X-Road System

**System**: X-Road system

**Level**: Summary

**Component:** Central server, Security server

**Actors**:

-   CS administrator – the administrator of the central server of the local X-Road instance.

-   SS administrator – the administrator of the security server that the organization wants to use for using or providing X-Road services.

-   Organization – an organization that wishes to start providing services on the X-Road or to use services provided by X-Road members.

**Brief Description**: SS administrator adds the organization's subsystem as a security server client and configures the signing keys and certificates of the organization. SS administrator initiates the registration of the organization's subsystem. The registration is completed by CS administrator. SS administrator configures the subsystem for using and/or providing services.

**Preconditions**: The use case assumes that the organization uses security server hosting services provided by another organization and that the used security server is registered in the X-Road central server.

**Postconditions**: A subsystem of the organization is registered as the security server client and ready to use and/or provide X-Road services.

**Trigger**: An organization wishes to start providing services on the X-Road or to use services provided by X-Road members.

**Main Success Scenario**:

1.  CS administrator registers the organization as an X-Road member: [2.3.7](#237-uc-member_10-add-an-x-road-member).

2.  SS administrator adds the organization's subsystem as a client of the security server: [2.4.4](#244-uc-member_47-add-a-client-to-the-security-server).

3.  SS administrator configures the tokens, keys and certificates for the organization's subsystem:

    -   connects the security tokens used for holding signing keys of the organization to the security server and initializes the tokens;

    -   creates a signing key for the organization: UC SS\_28 \[[UC-SS](#Ref_UC-SS)\];

    -   creates the certificate signing requests for the created signing key: UC SS\_29 \[[UC-SS](#Ref_UC-SS)\];

    -   forwards the certificate signing request to the organization. The organization forwards the certificate signing request to an approved certification service provider, receives the corresponding signing certificate and forwards the certificate to SS administrator.

    -   SS administrator imports the signing certificate to the security server: UC SS\_30 \[[UC-SS](#Ref_UC-SS)\].

4.  SS administrator initiates the registration of the organization's subsystem:

    -   sends a security server client request from the security server: [2.4.5](#245-uc-member_48-register-a-security-server-client) (the request is served by the central server: [2.3.25](#2325-uc-member_27-serve-a-management-service-request)) and

    -   sends a security server client request to the X-Road governing authority via out-of-band means.

5.  CS administrator completes the registration of the organization's subsystem:

    -   creates a security server client registration request: [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request) and

    -   approves the registration requests: [2.3.36](#2336-uc-member_37-approve-a-security-server-client-registration-request).

    -   The central server generates and distributes global configuration that contains the created registration relation between the security server and the subsystem: UC GCONF\_18 \[[UC-GCONF](#Ref_UC-GCONF)\].

6.  SS administrator waits for the security server to update configuration: UC GCONF\_23 \[[UC-GCONF](#Ref_UC-GCONF)\] and verifies that the state of the organization's subsystem is *registered*: [2.4.1](#241-uc-member_44-view-security-server-clients).

7.  In case the organization's subsystem is used in the service client role, SS administrator configures the settings for internal server communication: [2.4.6](#246-uc-member_49-change-a-security-server-clients-internal-server-connection-type), and adds internal TLS certificates to the subsystem if HTTPS connection is used: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate).

8.  In case the organization's subsystem is used in the service provider role, SS administrator

    -   adds internal TLS certificates to the subsystem if HTTPS connection is used to communicate with the internal servers: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate) and

    -   configures the services and access rights: \[[UC-SERVICE](#Ref_UC-SERVICE)\].

**Extensions**: -

**Related information**: -