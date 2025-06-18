#### 3.1.17 UC SERVICE\_15: Delete a WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator deletes a security server
client's WSDL or REST.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to delete a WSDL from the security
server client's list of WSDLs or RESTs.

**Main** **Success** **Scenario**:

1.  SS administrator selects to delete a WSDL or REST.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System deletes all information about the WSDL or REST, the services
    described in the WSDL or REST, and the access right records for the services
    described in the WSDL or REST from the system configuration.

5.  System logs the event “Delete service description” to the audit log.

**Extensions**:

- 3a. SS administrator terminates the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].