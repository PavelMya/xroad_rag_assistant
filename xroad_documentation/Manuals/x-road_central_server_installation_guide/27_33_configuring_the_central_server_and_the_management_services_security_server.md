### 3.3 Configuring the Central Server and the Management Services' Security Server

Upon the first configuration of the Central Server and the management services' Security Server, the following actions must be carried out.

Actions 7 and 8 must be performed in the management services' Security Server.

1. Generate the internal and external configuration signing keys. Refer to [UG-CS](#Ref_UG-CS) section „Generating a Configuration Signing Key“.
2. Configure the member classes. Refer to [UG-CS](#Ref_UG-CS) section „Managing the Member Classes“. (reference data: 2.4).
3. Configure the management service provider:
add the X-Road member who will be responsible for management services - [UG-CS](#Ref_UG-CS) section „Adding a Member“;
add the subsystem that will provide the management services to the X-Road member - [UG-CS](#Ref_UG-CS) section “Adding a Subsystem to an X-Road Member”;
appoint the subsystem as the management service provider - [UG-CS](#Ref_UG-CS) section “Appointing the Management Service Provider”.
4. Configure the certification services. Refer to [UG-CS](#Ref_UG-CS) section „Managing the Approved Certification Services“.
5. Configure the timestamping services. Refer to [UG-CS](#Ref_UG-CS) section „Managing the Approved Timestamping Services“.
6. Verify that the global configuration generation succeeds (no global error messages should be displayed in the user interface at this point) and download the internal configuration anchor - [UG-CS](#Ref_UG-CS) section “Downloading the Configuration Anchor”. The anchor is needed to set up the management services' Security Server.
7. Install and configure the management services' Security Server as described in [IG-SS](#Ref_IG-SS).
8. Register the management services' Security Server in the Central Server. Refer to [UG-SS](#Ref_UG-SS) section „Security Server Registration“.
9. Complete the registration of the management services' Security Server - [UG-CS](#Ref_UG-CS) section “Registering a Member's Security Server”.
10. Register the management service provider as a client of the management services' Security Server - [UG-CS](#Ref_UG-CS) section “Registering the Management Service Provider as a Security Server Client”.
11. Add the management service provider as a client to the management services' Security Server. Refer to [UG-SS](#Ref_UG-SS) section „Adding a Security Server Client”. (The client should appear in “Registered” state, as the association between the client and the Security Server was already registered in the Central Server in the previous step). If necessary, configure the signing keys and certificates for the client - [UG-SS](#Ref_UG-SS) section „Configuring a Signing Key and Certificate for a Security Server Client”
12. Configure the management services. Refer to [UG-CS](#Ref_UG-CS) section „Configuring the Management Services in The Management Services’ Security Server”.