#### 2.3.10 UC MEMBER\_13: Set Registration Request Status

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System looks for complementary request of the saved request. If one is found, the status of the requests is set to *submitted for approval*. If not, the status of the saved request is set to *waiting*.

**Preconditions**: -

**Postconditions**: The status of the saved request is set.

**Triggers**:

-   Step 10 of [2.3.9](#239-uc-member_12-add-an-owned-security-server-to-an-x-road-member).

-   Step 6 of [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request).

-   Step 6 of [2.3.21](#2321-uc-member_23-create-an-authentication-certificate-registration-request).

-   Step 11 of [2.3.26](#2326-uc-member_28-handle-an-authentication-certificate-registration-request).

-   Step 6 of [2.3.28](#2328-uc-member_30-handle-a-security-server-client-registration-request).

**Main Success Scenario**:

1.  System verifies that a complementary request for the saved request exists in the system.

2.  System sets the state of the saved request and the complementary request to *submitted for approval*.

3.  System adds the complementary request identifier to both of the registration requests.

**Extensions**:

1a. A complementary request for the saved request does not exist in the system.

  - 1a.1. System sets the status of the saved request to *waiting*.

  - 1a.2. Use case terminates.

**Related information**: -