#### 3.1.22 UC SERVICE\_20: Set the Option to Verify TLS Certificate of a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the TLS certificate
verification option of a service.

**Preconditions**: The protocol part of the service address is “https”.

**Postconditions**:

-   The SS administrator has changed the TLS certificate verification
    option.

-   An audit log record for the event is created.

**Trigger**: SS administrator wants to change the TLS certificate
verification option.

**Main** **Success** **Scenario**:

1.  SS administrator selects to change the TLS certificate verification
    option of a service.

2.  System saves the change.

3.  System logs the event “Edit service parameters” to the audit log.

**Extensions**: -

**Related** **information**:

-   If the option to verify the TLS certificate is set to “true”, the
    system will verify that the certificate that the client information
    system presented when setting up the TLS connection is previously
    saved in the system for the security server client providing the
    service.

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].