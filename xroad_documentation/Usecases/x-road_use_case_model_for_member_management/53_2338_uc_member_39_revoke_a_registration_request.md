#### 2.3.38 UC MEMBER\_39: Revoke a Registration Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator revokes a registration request that has been created in the central server. System creates a deletion request for the relation requested by the registration request.

**Preconditions**: The status of the registration request is *waiting*.

**Postconditions**: -

**Trigger**: An erroneously created registration request is discovered.

**Main Success Scenario**:

1.  CS administrator selects to revoke a registration request.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System creates and saves a deletion request for the relation requested by the registration request.

5.  System sets the state of the registration request to *revoked* and adds the identifier of the created deletion request to the registration request as the revoking request identifier.

6.  System displays the message “Successfully revoked X registration request with id 'Y'”, where “X” is either “client” or “authentication”, depending on the request type; and “Y” is the identifier of the declined request.

7.  System logs the event “Revoke authentication certificate registration request” or “Revoke client registration request”, depending on the type of the revoked request to the audit log.

**Extensions**:

3a. CS administrator decides not to revoke the request and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].