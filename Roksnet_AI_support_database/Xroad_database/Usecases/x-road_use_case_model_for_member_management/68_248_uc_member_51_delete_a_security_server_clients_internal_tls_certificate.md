#### 2.4.8 UC MEMBER\_51: Delete a Security Server Client's Internal TLS Certificate

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator deletes a security server Member Owner or a security server client's internal TLS certificate.

**Preconditions**: -

**Postconditions**: -

**Trigger**: -

**Main Success Scenario**:

1.  SS administrator selects to delete an internal TLS certificate of a security server owner or a security server client.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System deletes the certificate from system configuration.

5.  System logs the event “Delete internal TLS certificate” to the audit log.

**Extensions**:

3a. SS administrator decides not to delete the certificate and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].