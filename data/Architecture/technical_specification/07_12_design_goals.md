### 1.2 Design Goals

The following list contains main design goals and design decisions of the X-Road system.

-   X-Road is **decentralized** – the data exchange happens directly between organizations. There are no intermediaries. If the two organizations have established secure connection, the continuous data exchange depends only on availability of the organizations and the network between them.

-   **Ownership of data** – X-Road does not change ownership of data. The data owner (service provider) controls who can access particular services.

-   **Availability** is a central concern – the protocols are designed so that there is no single bottleneck in the system. Additionally, no component should become a single point of failure.

-   All the messages processed by the X-Road are usable as **digital evidence**. The technical solution must comply with requirements for digital seals according to eIDAS \[[EIDAS](#Ref_EIDAS)\]. This implies support for secure signature creation devices (SSCDs).

-   All the communication is implemented as \[[SOAP](#Ref_SOAP)\] or REST **service calls**. SOAP services are described using the \[[WSDL](#Ref_WSDL)\] language and REST services are described using the \[[OPENAPI](#Ref_OpenAPI)\] Specification v3.

-   **Cross-border services** – it is possible for an organization to invoke services provided by an organization belonging to a different instance of X-Road.

-   **Encapsulating the security protocol** – the security measures and the security protocol are encapsulated in standard components. The organizations are not required to implement security-related functionality for data exchange.

-   **Standardization** – X-Road aims to standardize the communication protocol between organizations. This enables the organizations to connect to any number of service providers without implementing additional protocols. X-Road core does not perform protocol and data conversion. If necessary, these conversions can be performed by the organization's information system.

-   **No predetermined roles** – once an organization has joined the X-Road infrastructure, it can act as both service client and service provider without having to perform any additional registration.

-   **Two-level authentication** – X-Road core handles authentication and access control on the organization level. End-user authentication is performed by information system of the service client.