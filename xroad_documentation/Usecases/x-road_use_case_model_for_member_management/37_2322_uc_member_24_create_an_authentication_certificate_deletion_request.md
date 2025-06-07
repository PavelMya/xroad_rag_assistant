#### 2.3.22 UC MEMBER\_24: Create an Authentication Certificate Deletion Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates an authentication certificate deletion request.

**Preconditions**: CS administrator is in possession of the information (the serial number of the authentication certificate and the X-Road identifier of the security server) needed to create the request.

**Postconditions**: -

**Trigger**: The owner of the security server has forwarded a request for deleting an authentication certificate of a security server to the X-Road governing authority.

**Main Success Scenario**:

1.  CS administrator selects to create an authentication certificate deletion request.

2.  System displays the prefilled authentication certificate registration request.

3.  CS administrator submits the request.

4.  System saves the request and deletes the authentication certificate.

5.  System displays the message: “Request of deleting authentication certificate from security server 'X' added successfully”, where “X” is the X-Road identifier of the security server.

6.  System logs the event “Delete authentication certificate of security server” to the audit log.

**Extensions**:

3a. CS administrator decides not to create the request and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].