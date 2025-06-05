#### 2.1.1 UC MEMBER\_01: Configure and Register a Security Server

**System**: X-Road system

**Level**: Summary

**Component:** Central server, Security server

**Actors**:

-   CS administrator – the administrator of the central server of the local X-Road instance.

-   SS administrator – the administrator of the security server owned by the X-Road member who wishes to register it's subsystem as a security server client.

**Brief Description**: SS administrator installs, initializes and configures a security server and obtains the signing certificate of the security server owner and the authentication certificate of the security server. SS administrator initiates the registration of the security server. CS administrator completes the registration of the security server.

**Preconditions**: The use case assumes that the organization that owns the security server is registered as an X-Road member (see [2.3.7](#237-uc-member_10-add-an-x-road-member)).

**Postconditions**: The security server is ready for registering clients and for exchanging X-Road messages.

**Trigger**: An X-Road member wishes to set up a security server.

**Main Success Scenario**:

1.  SS administrator installs and initializes a security server following the instructions given in the document “X-Road 7. Security Server Installation Guide” \[[IG-SS](#Ref_IG-SS)\].

2.  SS administrator adds one or more timestamping services for the security server: UC SS\_07 \[[UC-SS](#Ref_UC-SS)\].

3.  SS administrator configures the tokens, keys and certificates:

    -   connects the security tokens used for holding signing keys to the security server and initializes the tokens;

    -   creates a signing key for the security server owner and an authentication key for the security server: UC SS\_28 \[[UC-SS](#Ref_UC-SS)\];

    -   creates the certificate signing requests for the created signing key and authentication key: UC SS\_29 \[[UC-SS](#Ref_UC-SS)\];

    -   forwards the certificate signing requests to an approved certification service provider and receives the corresponding certificates;

    -   imports the signing certificate and the authentication certificate: UC SS\_30 \[[UC-SS](#Ref_UC-SS)\].

4.  SS administrator initiates the registration of the security server:

    -   sends an authentication certificate registration request from the security server: UC SS\_34 \[[UC-SS](#Ref_UC-SS)\] (the request is served by the central server: [2.3.25](#2325-uc-member_27-serve-a-management-service-request)) and

    -   sends an authentication certificate registration request to the X-Road governing authority via out-of-band means.

5.  CS administrator completes the registration of the security server:

    -   adds the security server as an owned server to the X-Road member: [2.3.9](#239-uc-member_12-add-an-owned-security-server-to-an-x-road-member) and

    -   approves the registration requests: [2.3.35](#2335-uc-member_36-approve-an-authentication-certificate-registration-request).

    -   The central server generates and distributes global configuration that contains the created registration relations between the security server owner and the security server, and between the security server and the authentication certificate: UC GCONF\_18 \[[UC-GCONF](#Ref_UC-GCONF)\].

6.  SS administrator waits for the security server to update configuration: UC GCONF\_23 \[[UC-GCONF](#Ref_UC-GCONF)\] and verifies that the state of the security server owner and the authentication certificate is *registered*: [2.4.1](#241-uc-member_44-view-security-server-clients) and UC SS\_19 \[[UC-SS](#Ref_UC-SS)\].

7.  SS administrator activates the authentication certificate: UC SS\_32 \[[UC-SS](#Ref_UC-SS)\].

**Extensions**: -

**Related information**: -