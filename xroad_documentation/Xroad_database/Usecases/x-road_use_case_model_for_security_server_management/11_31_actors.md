### 3.1 Actors

The X-Road security server management use case model includes the
following actor:

-   **SS administrator** (security server administrator) – a person
    responsible for managing the security server.

-   **Central server** – the central server of the X-Road instance. The
    central server provides management services for the security servers
    of this X-Road instance. The authentication certificate deletion
    requests are forwarded to the central server by the management
    services' security server. The authentication certificate
    registration request is sent directly to the central server by the
    security server that the certificate is to be registered for.

-   **Management services' security server** – a security server that
    has the management services' provider for this X-Road instance
    registered as a security server client.

The relationships between actors, systems and use cases are described in
Figure 1.

![](img/use_case_diagram_for_security_server_management.png)

Figure 1. Use case diagram for security server management