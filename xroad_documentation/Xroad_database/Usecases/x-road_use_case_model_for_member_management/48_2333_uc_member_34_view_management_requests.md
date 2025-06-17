#### 2.3.33 UC MEMBER\_34: View Management Requests

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of management requests.

**Preconditions**: -

**Postconditions**: The list of management requests saved in the system configuration has been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view management requests.

2.  System displays the list of management requests. The following information is displayed for each request.

    -   The identifier of the request.

    -   The date and time of when the management request was saved to the system configuration.

    -   The type of the request:

        -   *certificate registration* for authentication certificate registration requests;

        -   *certificate deletion* for authentication certificate deletion requests;

        -   *client registration* for security server client registration requests;

        -   *client deletion* for security server client deletion requests.

    -   The source of the request

        -   *Security server* for the requests that have been submitted to the central server through a security server; and

        -   *X-Road center* for the requests that have been created in the central server.

    -   The name of the owner of the server that is the subject of the request.

    -   The X-Road identifier of the server that is the subject of the request.

    -   The status of the request (for registration requests).

    The following user action options are displayed:

    -   view the details of a management request: [2.3.34](#2334-uc-member_35-view-the-details-of-a-management-request).

**Extensions**: -

**Related information**:

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].