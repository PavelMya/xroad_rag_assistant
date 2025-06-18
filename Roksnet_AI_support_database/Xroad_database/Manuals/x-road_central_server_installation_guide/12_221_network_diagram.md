#### 2.2.1 Network Diagram

The network diagram below provides an example of a basic Central Server setup.

![network diagram](img/ig-cs_network_diagram.svg)

The table below lists the required connections between different components. Please note that required connections between Security Servers and trust services (OCSP service, time-stamping service) have been omitted from the diagram and the table below. Their configuration is described in [IG-SS](#Ref_IG-SS).

| **Connection Type** | **Source**                        | **Target**                    | **Target Ports**    | **Protocol** | **Note**                                                                                                                                                                         |
|---------------------|-----------------------------------|-------------------------------|---------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Out                 | Monitoring Security Server        | X-Road Member Security Server | 5500, 5577          | tcp          | Operational and environmental monitoring data collection                                                                                                                         |
| In                  | X-Road Member Security Server     | Central Server                | 80, 443             | tcp          | Global configuration distribution                                                                                                                                                |
| In                  | X-Road Member Security Server     | Central Server                | 4001                | tcp          | Authentication certificate registration requests from X-Road Members' Security Servers                                                                                           |
| In                  | Management Security Server        | Central Server                | 80, 443, 4001, 4002 | tcp          | Source in the internal network. Management service requests from Management Security Server. Global configuration distribution. Authentication certificate registration requests |
| In                  | Monitoring Security Server        | Central Server                | 80, 443, 4001       | tcp          | Source in the internal network. Global configuration distribution. Authentication certificate registration requests                                                              |
| In                  | X-Road Member Security Server     | Management Security Server    | 5500, 5577          | tcp          | Management service requests from X-Road Members' Security Servers                                                                                                                |
| In                  | Central Monitoring Client         | Monitoring Security Server    | 8080, 8443          | tcp          | Source in the internal network                                                                                                                                                   |
| In                  | Admin, management REST API client | Central Server                | 4000                | tcp          | Source in the internal network                                                                                                                                                   |
| In                  | Admin                             | Management Security Server    | 4000                | tcp          | Source in the internal network                                                                                                                                                   |
| In                  | Admin                             | Monitoring Security Server    | 4000                | tcp          | Source in the internal network                                                                                                                                                   |

The table below lists the open ports for Central Server components utilizing the _loopback_ interface. A loopback interface is a virtual network interface on a computer, facilitating self-communication for processes and applications. This enables local communication and the ports must be accessible locally.

| **Component**        | **Ports** | **Protocol** | **Note**                                      |
|----------------------|-----------|--------------|-----------------------------------------------|
| Registration Service | 8084      | tcp          | For incoming requests to Registration Service |
| Management Service   | 8085      | tcp          | For incoming requests to Management Service   |
| PostgreSQL database  | 5432      | tcp          | Default PostgreSQL database port              |
| Signer               | 5560      | tcp          | Signer gRPC port                              |
| Audit log            | 514       | udp          |                                               |