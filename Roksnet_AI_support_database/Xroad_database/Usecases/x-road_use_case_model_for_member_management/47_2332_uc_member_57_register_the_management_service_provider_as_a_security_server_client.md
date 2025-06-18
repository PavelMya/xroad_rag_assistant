#### 2.3.32 UC MEMBER\_57: Register the Management Service Provider as a Security Server Client

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates a registration request for registering the management service provider as a security server client. System saves the registration relation.

**Preconditions**:

-   The management service provider is not registered as a client of any security servers.

-   The security server where the management service provider will be registered exists in the system configuration.

**Postconditions**: -

**Trigger**: The management service provider needs to be registered as a client of the management services' security server to set up (bootstrap) the management services on the initial configuration of an X-Road instance.

**Main Success Scenario**:

1.  CS administrator selects to register the management service provider as a security server client.

2.  System displays a security server client registration request, prefilling the client's values with the management service provider's information.

3.  CS administrator selects the security server where the management service provider will be registered from the list of security servers registered in the central server and submits the request.

4.  System saves the security server client registration request and sets the status of the request to *approved*.

5.  System saves the registration relation between the management service provider and the security server to system configuration.

6.  System displays the message: “Management service provider 'X' registered as security server 'Y' client”, where “X” is the X-Road identifier of the management service provider and “Y” is the X-Road identifier of the security server.

7.  System logs the event “Register management service provider as security server client” to the audit log.

**Extensions**:

3a. CS administrator selects not to submit the request and terminates the use case.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].