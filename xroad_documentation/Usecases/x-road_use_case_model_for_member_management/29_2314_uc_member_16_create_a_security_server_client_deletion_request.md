#### 2.3.14 UC MEMBER\_16: Create a Security Server Client Deletion Request

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates a security server client deletion request to delete the registration of a client of a security server.

**Preconditions**: CS administrator is in possession of the information (the X-Road identifier of the client to be deleted and the X-Road identifier of the security server) needed to delete the registration of an X-Road member's subsystem as a client of a security server.

**Postconditions**: -

**Trigger**: The X-Road member has forwarded a request for deleting the registration to the X-Road governing authority.

**Main Success Scenario**:

1.  CS administrator selects to create a security server client deletion request for a subsystem of an X-Road member.

2.  System displays a prefilled security server client deletion request.

3.  CS administrator submits the request.

4.  System saves the request and deletes the registration relation between the client and the security server.

5.  System displays the message: “Request of deleting client 'X' from security server 'Y' added successfully”, where “X” is the X-Road identifier of the subsystem and “Y” is the X-Road identifier of the security server.

6.  System logs the event “Unregister member as security server client” to the audit log.

**Extensions**:

3a. CS administrator selects to terminate the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The protocol for management services is described the document “X-Road: Protocol for Management Services” \[[PR-MSERV](#Ref_PR-MSERV)\].