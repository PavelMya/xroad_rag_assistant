### 2.2 Actors

The use case model for X-Road member management includes the following actors.

-   **SS administrator** (security server administrator) – a person responsible for managing the security server.

-   **CS administrator** (central server administrator) – a person responsible for managing the central server.

-   **Security server** – a security server that sends management service requests to the central server. The authentication certificate deletion requests, and security server client registration and deletion requests are forwarded to the central server by the management services' security server. The authentication certificate registration request is sent directly to the central server by the security server that the certificate is to be registered for.

-   **Management services' security server** – a security server that has the management services' provider for this X-Road instance registered as a security server client.

Relationships between the actors, systems and use cases are described in [Figure 1](#Ref_Use_case_diagram_for_member_management).


<a id="Ref_Use_case_diagram_for_member_management" class="anchor"></a>
![](img/uc-member_use_case_diagram_for_member_management.png)

Figure 1. Use case diagram for member management