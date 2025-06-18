#### 3.1.24 UC SERVICE\_22: Apply the Parameter Value of a Service to All the Services in the WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator applies the value of a
service parameter (address, timeout, TLS certificate verification) of
one service to all the services in the WSDL or REST where the service is
described.

**Preconditions**: -

**Postconditions**:

-   The value of a service parameter is identical for all the services
    in a WSDL or REST. The TLS certificate verification option is changed only
    for the services where the protocol part of the service address is
    “https”.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to apply the parameter value of one
service to all the services in the WSDL or REST where the service is described.

**Main** **Success** **Scenario**:

1.  SS administrator selects to apply a service parameter value to all
    the services in the WSDL or REST.

2.  System saves the parameter value for every service described in the
    same WSDL or REST.

3.  System logs the event “Edit service parameters” to the audit log.

**Extensions**: -

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].