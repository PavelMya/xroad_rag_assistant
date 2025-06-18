## 2 Overview matrix of the X-Road technology

[Table 1](#Ref_Technology_matrix_of_the_X_Road) presents the list of technologies used in the X-Road and mapping between the technologies and X-Road components.


Table 1. Technology matrix of the X-Road

| **Technology**                     | **Security Server** | **Central Server** | **Configuration proxy** | **Operational Monitoring Daemon** |
|------------------------------------|:-------------------:|:------------------:|:-----------------------:|:---------------------------------:|
| Java 21                            |          X          |         X          |            X            |                 X                 |
| C                                  |          X          |         X          |                         |                                   |
| Logback                            |          X          |         X          |            X            |                 X                 |
| gRPC                               |          X          |         X          |            X            |                 X                 |
| Jetty 11                           |  X\[[3](#Ref_3)\]   |  X\[[4](#Ref_4)\]  |                         |                                   |
| Ubuntu 20.04                       |          X          |         X          |            X            |                 X                 |
| Ubuntu 22.04                       |          X          |         X          |            X            |                 X                 |
| Red Hat Enterprise Linux 7 (RHEL7) |          X          |                    |                         |                 X                 |
| Red Hat Enterprise Linux 8 (RHEL8) |          X          |                    |                         |                 X                 |
| Red Hat Enterprise Linux 9 (RHEL9) |          X          |                    |                         |                 X                 |
| PostgreSQL 12+\[[5](#Ref_5)\]      |          X          |         X          |                         |                 X                 |
| nginx                              |                     |         X          |            X            |                                   |
| PAM                                |          X          |         X          |                         |                                   |
| Liquibase 4                        |          X          |         X          |                         |                 X                 |
| systemd                            |          X          |         X          |            X            |                 X                 |
| PKCS \#11\[[2](#Ref_2)\]           |          X          |         X          |            X            |                                   |
| Dropwizard Metrics 4               |          X          |                    |                         |                 X                 |
| Spring Boot 3                      |          X          |         X          |                         |                                   |
| Vue.js 3                           |          X          |         X          |                         |                                   |
| Npm 8                              |          X          |         X          |                         |                                   |
| Node 18                            |          X          |         X          |                         |                                   |
| Typescript                         |          X          |         X          |                         |                                   |
| OpenAPI 3                          |          X          |         X          |                         |                                   |
| Embedded Tomcat 10                 |          X          |         X          |                         |                                   |
| GNU Privacy Guard                  |          X          |         X          |                         |                                   |

See [[ARC-G]](#ARC-G) for general X-Road architecture details.


\[2\] The use of hardware cryptographic devices requires that a PKCS \#11 driver is installed and configured in the system.


\[3\] Security Server uses embedded Jetty for clientproxy, serverproxy and OCSP responder.


\[4\] Central Server uses embedded Jetty for management service and registration service.


\[5\] PostgreSQL version varies depending on operating system. By default, RHEL7 uses version 9, RHEL8 - 10, RHEL9 - 13, Ubuntu 20.04 - 12, Ubuntu 22.04 - 14. User may also use external PostgreSQL server.