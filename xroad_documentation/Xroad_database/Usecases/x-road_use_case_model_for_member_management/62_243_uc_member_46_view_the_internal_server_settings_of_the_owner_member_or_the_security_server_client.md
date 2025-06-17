#### 2.4.3 UC MEMBER\_46: View the Internal Server Settings of the Owner Member or the security Server client

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator view the settings for the internal servers of the Owner Member.

**Preconditions**: -

**Postconditions**: The settings for the internal servers of the Owner Member or the security Server client have been displayed to SS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to view the settings for the internal servers of the Owner Member or the security Server client.

2.  System displays the following information:

    -   the connection type for the internal servers that act as service clients (for security server owner the connection type is set to HTTPS by default);

    -   the list of internal TLS certificates saved for the Owner Member or the security Server client. The SHA-1 hash value of the certificate is displayed for each certificate.
    
    -   the Security Server certificate

    The following user action options are displayed:

    -   change the connection type for the security server owner or security server client's internal servers that act as service clients: [2.4.6](#246-uc-member_49-change-a-security-server-clients-internal-server-connection-type);

    -   view the details of an internal TLS certificate: [2.5.2](#252-uc-member_55-view-certificate-details);

    -   add an internal TLS certificate: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate);

    -   delete an internal TLS certificate: [2.4.8](#248-uc-member_51-delete-a-security-server-clients-internal-tls-certificate);
    
    -   export the Security Server certificate

**Extensions**: -

**Related information**: -