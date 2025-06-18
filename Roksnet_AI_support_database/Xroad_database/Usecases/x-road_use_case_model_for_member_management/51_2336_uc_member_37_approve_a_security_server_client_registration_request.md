#### 2.3.36 UC MEMBER\_37: Approve a Security Server Client Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator approves a security server client registration request. System sets the statuses of the complementary requests to *approved*, and saves the registration relation between the security server client and the security server.

**Preconditions**: The status of the complementary pair of registration requests is *submitted for approval*.

**Postconditions**: -

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to approve a security server client registration request.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System saves the registration relation between the security server client and the security server.

5.  System sets the state of the complementary requests to *approved*.

6.  System logs the event “Approve registration request” to the audit log.

**Extensions**:

3a. CS administrator decides not to approve the request and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].