#### 2.3.35 UC MEMBER\_36: Approve an Authentication Certificate Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator approves an authentication certificate registration request. System sets the statuses of the complementary requests to *approved*. System registers the security server as an owned server of the X-Road client that sent the request, if the security server was not previously registered. System saves the authentication certificate and the registration relation between the certificate and the security server.

**Preconditions**: The status of the complementary pair of registration requests is *submitted for approval*.

**Postconditions**: -

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to approve an authentication certificate registration request.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System verifies that a security server with the identifier specified in the registration request is registered as an owned server of the X-Road member that sent the registration request.

5.  System saves the authentication certificate and the registration relation between the certificate and the security server.

6.  System sets the state of the complementary requests to *approved*.

7.  System logs the event “Approve registration request” to the audit log.

**Extensions**:

3a. CS administrator decides not to approve the request and terminates the use case.

4a. The security server is not registered as an owned server of the X-Road member that sent the registration request.

  - 4a.1. System saves the security server information found in the registration request to the system configuration as an owned security server of the X-Road member.

  - 4a.2. Use case continues from step 5.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].