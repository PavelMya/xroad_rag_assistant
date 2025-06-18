### 9.1 Communication with Service Consumer Information Systems

A Security Server can be configured to require either the HTTP, HTTPS, or HTTPS with Client Authentication (i.e. HTTP over mTLS) protocol from the consumer role information systems for communication.

- HTTP protocol should be used if the consumer information system and the Security Server communicate in a private network segment where no other computers are connected to. Furthermore, the information system must not allow interactive log-in.


- HTTPS NOAUTH - a.k.a plain HTTPS protocol should be used if it is not possible to provide a separate network segment for the communication between the information system and the Security Server. In that case, cryptographic methods are used to protect their communication against potential eavesdropping and interception.


- HTTPS - a.k.a. HTTPS with Client Authentication protocol (**default for new clients**) should be used to protect against unauthorised communication in addition to potential eavesdropping and interception. Before HTTPS can be used, internal TLS certificates must be created for the information systems and uploaded to the Security Server.

**By default the connection type for all the Security Server clients is set to HTTPS to prevent unauthorised use of the clients.**

**It is strongly recommended to keep the connection type of the Security Server owner as HTTPS to prevent Security Server clients from making operational monitoring data requests as a Security Server owner.**

To set the connection method for information systems in the **service consumer role**, follow these steps:

1. In the **Navigation tabs**, select **CLIENTS**, select a Security Server owner or a client from the table

2. In the view that opens, select the **INTERNAL SERVERS** tab

3. On the **Connection type** drop-down, select the connection method between HTTP, HTTPS NOAUTH or HTTPS. The changes will be saved immediately on selecting the new method and a "Connection type updated" message is displayed.


   **Note:** If the HTTP connection method is selected, but the information system connects to the Security Server over HTTPS, then the connection is accepted, but the client's internal TLS certificate is not verified (same behavior as with HTTPS NOAUTH).

   **Note:** If HTTPS NOAUTH method is selected keep in mind that the consumer information system must trust the Security Server's TLS certificate. This can be achieved by exporting Security Server's internal TLS certificate into information system's truststore (see section [9.3](#93-managing-information-system-tls-certificates)).

   **Note:** If HTTPS method is selected then additionally the client information system's TLS certificate must be trusted. In order to accomplish that the certificate must be added into Security Server's **Information System TLS certificate** list (see section [9.3](#93-managing-information-system-tls-certificates)).

Depending on the configured connection method, the request URL for information system is **`http://SECURITYSERVER/`** or **`https://SECURITYSERVER/`**. When making the request, the address `SECURITYSERVER` must be replaced with the actual address of the Security Server.