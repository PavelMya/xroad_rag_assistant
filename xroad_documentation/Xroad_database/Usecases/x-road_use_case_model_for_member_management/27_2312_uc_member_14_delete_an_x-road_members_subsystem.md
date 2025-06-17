#### 2.3.12 UC MEMBER\_14: Delete an X-Road Member's Subsystem

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief description**: CS administrator deletes a subsystem of an X-Road member.

**Precondition**: The subsystem is not registered as a security server client.

**Postcondition**: -

**Trigger**: -

**Main success scenario**:

1.  CS administrator selects to delete a subsystem of an X-Road member.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System verifies that the subsystem is a member of one or more global groups and deletes the respective group membership records from the system configuration.

5.  System deletes the subsystem from the system configuration.

6.  System logs the event “Delete subsystem” to the audit log.

**Extensions:**

3a. CS administrator selects not to delete the subsystem and terminates the use case.

4a. The subsystem is not a member of any global groups.

  - 4a.1. Use case continues from step 5.

**Related information:**

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].