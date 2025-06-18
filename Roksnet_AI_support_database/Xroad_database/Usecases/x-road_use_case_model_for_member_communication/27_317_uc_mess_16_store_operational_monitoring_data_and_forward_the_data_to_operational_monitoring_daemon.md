### 3.17 UC MESS\_16: Store Operational Monitoring Data and Forward the Data to Operational Monitoring Daemon

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: Security server stores operational monitoring data in operational monitoring buffer. One operational monitoring data record is created for each request during the message exchange. Security server forwards operational data stored in operational monitoring buffer to operational monitoring daemon. Successfully forwarded records are removed from the operational monitoring buffer.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 22 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

-   Step 20 of [3.4](#34-uc-mess_03-process-x-road-request-message).

-   The time interval for periodical sending of operational monitoring data has passed.

**Main Success Scenario**:

1.  System stores the following data in the operational monitoring buffer (the fields not marked as mandatory are optional):

    -   the internal IP of the security server (mandatory);

    -   type of the security server (either *Client* or *Producer*, mandatory);

    -   request in timestamp (In the client's security server: the Unix timestamp in milliseconds when the request was received by the client's security server. In the service provider's security server: the Unix timestamp in milliseconds when the request was received by the service provider's security server. Mandatory.);

    -   request out timestamp (In the client's security server: the Unix timestamp in milliseconds when the request was sent out from the client's security server to the client's information system. In the service provider's security server: the Unix timestamp in milliseconds when the request was sent out from the service provider's security server. If the request is either a metadata request or a proxy monitoring data request the value of the parameter is equal to ‘request in timestamp’);

    -   response in timestamp (In the client's security server: the Unix timestamp in milliseconds when the response was received by the client's security server. In the service provider's security server: the Unix timestamp in milliseconds when the response was received by the service provider's security server. If the request is either a metadata request or a proxy monitoring data request the value of the parameter is equal to ‘response out timestamp’);

    -   response out timestamp (In the client's security server: the Unix timestamp in milliseconds when the response was sent out from the client's security server to the client's information system. In the service provider's security server: the Unix timestamp in milliseconds when the response was sent out from the service provider's security server. Mandatory.);

    -   the X-Road instance identifier of the instance used by the client;

    -   the member class of the X-Road member (client);

    -   the member code of the X-Road member (client);

    -   the subsystem code of the X-Road member (client);

    -   the X-Road instance identifier of the instance used by the service provider;

    -   the member class of the X-Road member (service provider);

    -   the member code of the X-Road member (service provider);

    -   the subsystem code of the X-Road member (service provider);

    -   the code of the service;

    -   the version number of the service;

    -   the class of the represented party;

    -   the code of the represented party;

    -   the unique identifier of the message;

    -   the personal code of the client that initiated the request;

    -   the client's internal identifier of the message;

    -   the version of the X-Road message protocol;

    -   the external address of client's security server (IP or host name) defined in global configuration;

    -   the external address of service provider's security server (IP or host name) defined in global configuration;

    -   the size of the request (bytes);

    -   the size of the MIME-container of the request (bytes);

    -   the number of attachments of the request;

    -   the size of the response (bytes);

    -   the size of the MIME-container of the response (bytes);

    -   the number of attachments of the response;

    -   the indication of successful/unsuccessful request mediation (boolean; mandatory);

    -   SOAP fault code;

    -   SOAP fault reason.

2.  System verifies how many records there are in operational monitoring buffer and composes a JSON message.

3.  System verifies that the operational monitoring daemon should be connected using HTTP protocol. System initiates a connection with the operational monitoring daemon.

4.  System forwards the operational data record(s) to the operational monitoring daemon. The number of records included in one message is defined by a system parameter.

5.  System receives an acknowledgement from operational monitoring daemon.

6.  System removes successfully forwarded record(s) from operational monitoring buffer.

7.  System verifies that there are no more records in operational monitoring buffer.

**Extensions**:

1a. The size limit of the operational monitoring buffer has been exceeded.

  - 1a.1. System removes the oldest record from the operational monitoring buffer and logs a warning message: “Operational monitoring buffer overflow, removing the eldest record ‘X’”, where “X” is the index of the record in operational monitoring buffer.

  - 1a.2. Use case continues from step 1.

1b. The time interval for periodical sending of operational monitoring data (defined by a system parameter) has passed.

  - 1b.1. Use case continues from step 2.

2a. System verifies that the process of sending operational data to operational monitoring daemon is not finished.

  - 2a.1. Use case terminates.

2b. System verifies that there are no operational monitoring records in operational monitoring buffer.

  - 2b.1. Use case terminates.

3a. System fails to initiate a connection with the operational monitoring daemon.

  - 3a.1. System logs an error message. The use case terminates.

3b. System verifies that the operational monitoring daemon should be connected using HTTPS and the operational monitoring daemon certificate should be verified.

  - 3b.1. System uses the internal TLS certificate of the security server for connection.

  - 3b.2. System finds the operational monitoring daemon TLS certificate from the connection.

    - 3b.2a. System fails to find the TLS certificate.

      - 3b.2a.1. System logs an error message. The use case terminates.

  - 3b.3. System verifies that the TLS certificate sent by the operational monitoring daemon matches the TLS certificate configured for the operational monitoring daemon in the system configuration. Use case continues from step 4.

    - 3b.3a. System does not find the TLS certificate for the operational monitoring daemon from the system configuration.

      - 3b.3a.1. System logs an error message. The use case terminates.

    - 3b.3b. TLS certificate configured for the operational monitoring daemon does not match the certificate the operational monitoring daemon presented for TLS authentication.

      - 3b.3b.1. System logs an error message. The use case terminates.

5a. Storing operational monitoring data in operational monitoring daemon failed.

  - 5a.1. Use case terminates.

6a. System verifies that there are more records in operational monitoring buffer.

  - 6a.1. Use case continues from step 3.

**Related information**: The functionality of operational monitoring daemon is described in \[[UC-OPMON](#Ref_UC-OPMON)\].

## Annex A Sequence Diagram for Messaging

![](img/uc-mess_annex_a_sequence_diagram_for_messaging.png)