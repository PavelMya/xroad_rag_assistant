#### 2.3.37 UC MEMBER\_38: Decline a Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator declines a pair of complementary registration requests.

**Preconditions**: The state of the pair of complementary registration requests is *submitted for approval*.

**Postconditions**: -

**Trigger**:

**Main Success Scenario**:

1.  CS administrator selects to decline a registration request.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System sets the state of the request and the complementary request to *declined*.

5.  System displays the message “Successfully declined request with id 'X'”, where “X” is the identifier of the declined request.

6.  System logs the event “Decline registration request” to the audit log.

**Extensions**:

3a. CS administrator decides not to decline the request and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].