### 3.1 Actors

The X-Road member communication use case model includes the following actors.

-   **Client IS** (service client's information system) – a subsystem of an X-Road member acting as a service client in an X-Road service call event.

-   **Client SS** (service client's security server) – X-Road security server where the service client's information system is registered as a client of this security server.

-   **Provider IS** (service provider's information system) – a subsystem of an X-Road member acting as a service provider in an X-Road service call event.

-   **Provider SS** (service provider's security server) – X-Road security server where the service provider's information system is registered as a client of this security server.

-   **TSS** (timestamping server) – a timestamping service approved by the X-Road and configured to be used by the Client SS and Provider SS.

-   **OCSP responder** – OCSP service providing OCSP responses for the approved certification service that issued the certificates used by the Client SS and Provider SS.

Relationships between actors, systems and use cases are described in [Figure 1](#Ref_Communication_use_case_diagram).


<a id="Ref_Communication_use_case_diagram" class="anchor"></a>
![](img/uc-mess_communication_use_case_diagram.png)

Figure 1. Communication use case diagram