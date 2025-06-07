#### 2.4.35 UC MEMBER\_46: View the Internal Server Settings of a Security Server Client

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator view the settings for the internal servers of a security server owner or a security server client.

**Preconditions**: -

**Postconditions**: The settings for the internal servers of a security server owner or a security server client have been displayed to SS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to view the settings for the internal servers of a security server owner or a security server client.

2.  System displays the following information:

    -   the connection type for the a security server owner or security server client's internal servers that act as service clients (for security server owner the connection type is set to HTTPS by default);

    -   the list of internal TLS certificates saved for the owner or the client. The SHA-1 hash value of the certificate is displayed for each certificate.

    The following user action options are displayed:

    -   change the connection type for the security server owner or security server client's internal servers that act as service clients: [2.4.6](#246-uc-member_49-change-a-security-server-clients-internal-server-connection-type);

    -   view the details of an internal TLS certificate: [2.5.2](#252-uc-member_55-view-certificate-details);

    -   add an internal TLS certificate: [2.4.7](#247-uc-member_50-add-a-security-server-clients-internal-tls-certificate);

    -   delete an internal TLS certificate: [2.4.8](#248-uc-member_51-delete-a-security-server-clients-internal-tls-certificate);

**Extensions**: -

**Related information**: -