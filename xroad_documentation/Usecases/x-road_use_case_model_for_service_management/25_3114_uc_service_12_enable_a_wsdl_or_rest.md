#### 3.1.14 UC SERVICE\_12: Enable a WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator enables a WSDL or REST. The services
included in the WSDL or REST will be available for the service clients.

**Preconditions**: The WSDL or REST is disabled.

**Postconditions**:

-   The WSDL or REST has been enabled.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants make the services described in a
WSDL available for the service clients.

**Main** **Success** **Scenario**:

1.  SS administrator selects to enable a WSDL or REST.

2.  System activates the WSDL or REST.

3.  System logs the event “Enable service description” to the audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events \[[SPEC-AL](#Ref_SPEC-AL)\].