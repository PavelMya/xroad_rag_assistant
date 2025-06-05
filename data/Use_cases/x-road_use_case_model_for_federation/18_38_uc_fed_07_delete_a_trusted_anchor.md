### 3.8 UC FED\_07: Delete a Trusted Anchor 

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes a trusted anchor. The
anchor is removed from the list of configuration sources distributed to
the security servers of this X-Road instance via the global
configuration.

**Preconditions**: A trusted anchor has been uploaded to the system.

**Postconditions**: -

**Trigger**: A federation relationship is terminated.

**Main success scenario**:

1.  CS administrator selects to delete a trusted anchor.

2.  System prompts for confirmation.

3.  CS administrator confirms the deletion.

4.  System deletes the selected configuration anchor and displays the
    message “Configuration anchor of instance 'X' deleted
    successfully.”, where “X” is the instance identifier of the X-Road
    instance the deleted anchor originated from.

5.  System logs the event “Delete trusted anchor” to the audit log.

**Extensions**:

- 3a. CS administrator selects to terminate the use case.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].