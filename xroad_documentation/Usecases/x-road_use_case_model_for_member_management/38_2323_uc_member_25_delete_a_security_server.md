#### 2.3.23 UC MEMBER\_25: Delete a Security Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes a security server. System generates deletion requests for the clients and authentication certificates registered for the deleted server.

**Preconditions**: CS administrator is in possession of the information (X-Road identifier of the security server) needed to delete the server.

**Postconditions**: -

**Triggers**:

-   The owner of the security server has forwarded a request for deleting the security server to the X-Road governing authority.

-   Step 4a.1 of [2.3.24](#2324-uc-member_26-delete-an-x-road-member).

**Main Success Scenario**:

1.  CS administrator selects to delete a security server.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System verifies that the security server has no registered clients (except for the owner).

5.  System verifies that the security server has no registered authentication certificates.

6.  System deletes the security server from the system configuration.

7.  System logs the event “Delete security server” to the audit log.

**Extensions**:

3a. CS administrator decides not to delete the security server and terminates the use case.

4a. The security server has registered clients (other than the owner). For each registered client:

  - 4a.1. system creates and saves a security server client deletion request with the comment “'X' deletion”, where “X” is the X-Road identifier of the security server to be deleted;

  - 4a.2. system deletes the registration relation between the client and the security server.

  - 4a.3. Use case continues from step 5.

5a. The security server has registered authentication certificates. For each registered certificate:

  - 5a.1. system creates and saves an authentication certificate deletion request with the comment “'X' deletion”, where “X” is the X-Road identifier of the security server to be deleted;

  - 5a.2. system deletes the authentication certificate.

  - 5a.3. Use case continues from step 6.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].