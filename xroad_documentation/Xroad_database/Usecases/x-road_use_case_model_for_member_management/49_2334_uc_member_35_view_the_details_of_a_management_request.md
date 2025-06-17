#### 2.3.34 UC MEMBER\_35: View the Details of a Management Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator view the details of a management request.

**Preconditions**: -

**Postconditions**: The details of the management request have been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the details of a management request.

2.  System displays the following information.

    -   Information about the request:

        -   the identifier of the request;

        -   the date and time of saving the request in the central server;

        -   the source of the request. The request can be either submitted through a security server (SECURITY\_SERVER) or created in the central server (CENTER);

        -   the identifier of the request that caused the status change of the request from *waiting* to *submitted for approval* or from *waiting* to *revoked*;

        -   a comment about the source event for the generation of the request. For example, when a security server is deleted from the central server, deletion requests are automatically generated for all the clients and authentication certificates of this security server. In the “Comments” field of the generated request, a comment with the server identifier is added in such case.

    -   Information about the security server associated with the request:

        -   the name, member class and member code of the security server owner;

        -   the code of the security server;

        -   the address of the security server. This field is filled only for authentication certificate registration requests submitted through a security server, and only if the security server's administration deemed it necessary to provide an address upon request submission.

    -   Information about the request object – that is, client or authentication certificate being registered or deleted.

    For an authentication certificate:

    -   the name of the certification authority who issued the certificate;

    -   the serial number of the certificate;

    -   the attributes of the certificate's subject field;

    -   the expiration date of the certificate.

    For a security server client:

    -   the name of the client (the name of the X-Road member responsible for the subsystem submitted for registration or unregistration with this request);

    -   the member class, member code and subsystem code of the client.

    The following user action options are displayed:

    -   approve a pair of complementary registration requests: [2.3.35](#2335-uc-member_36-approve-an-authentication-certificate-registration-request);

    -   decline a pair of complementary registration requests: [2.3.37](#2337-uc-member_38-decline-a-registration-request);

    -   revoke a registration request created in the central server: [2.3.38](#2338-uc-member_39-revoke-a-registration-request).

**Extensions**: -

**Related information**: -