#### 2.3.24 UC MEMBER\_26: Delete an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes an X-Road member.

**Preconditions**: The X-Road membership contract between the organization registered as an X-Road member and the X-Road governing agency has been terminated.

**Postconditions**: -

**Trigger**: The X-Road membership contract between the organization registered as an X-Road member and the X-Road governing agency is terminated.

**Main Success Scenario**:

1.  CS administrator selects to delete an X-Road member.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System verifies that the member has no owned security servers.

5.  System verifies that the member's subsystems are not clients of any security servers.

6.  System verifies that the member or the member's subsystems do not belong to any global groups.

7.  System deletes the member and the member's subsystems (if any exist) from the system configuration.

8.  System logs the event “Delete member” to the audit log.

**Extensions**:

3a. CS administrator decides not to delete the security server and terminates the use case.

4a. The member has owned security servers. For each owned security server:

  - 4a.1. system deletes the security server: steps 4-6 of [2.3.23](#2323-uc-member_25-delete-a-security-server);

  - 4a.2. use case continues from step 5.

5a. The member's subsystems are clients of security servers. For each security server client registration relation:

  - 5a.1. system creates and saves a security server client deletion request with the comment “'X' deletion”, where “X” is the X-Road identifier of the X-Road member that is being deleted;

  - 5a.2. system deletes the registration relation between the client and the security server;

  - 5a.3. use case continues from step 6.

6a. The member or member's subsystems belong to global groups.

  - 6a.1. System removes the member or member's subsystems from global groups.

  - 6a.2. Use case continues from step 7.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].