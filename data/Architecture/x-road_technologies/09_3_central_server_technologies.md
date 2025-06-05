## 3 Central Server technologies

[Table 2](#Ref_Technology_matrix_of_the_central_server) presents the list of technologies used in the Central Server and the mapping between technologies and Central Server components.

<a id="Ref_Technology_matrix_of_the_central_server" class="anchor"></a>
Table 2. Technology matrix of the Central Server

| **Technology**                | **Signer** | **Password Store** | **Management/Registration Service** | **Database** | **User Interface** | **Rest API** | **Backend Scripts** | **Configuration Client** |
|-------------------------------|:----------:|:------------------:|:-----------------------------------:|:------------:|:------------------:|:------------:|:-------------------:|:------------------------:|
| Java 21                       |     X      |                    |                  X                  |              |                    |      X       |                     |            X             |
| C                             |            |         X          |                                     |              |                    |              |                     |                          |
| Logback                       |     X      |                    |                  X                  |              |                    |      X       |                     |            X             |
| gRPC                          |     X      |                    |                                     |              |                    |      X       |                     |                          |
| Embedded Jetty 11             |            |                    |                  X                  |              |                    |              |                     |                          |
| Embedded Tomcat 10            |            |                    |                                     |              |                    |      X       |                     |                          |
| Spring Boot 3                 |            |                    |                  X                  |              |                    |      X       |                     |                          |
| Vue.js 3                      |            |                    |                                     |              |         X          |              |                     |                          |
| Npm 8                         |            |                    |                                     |              |         X          |              |                     |                          |
| Node 18                       |            |                    |                                     |              |         X          |              |                     |                          |
| Typescript                    |            |                    |                                     |              |         X          |              |                     |                          |
| OpenAPI 3                     |            |                    |                  X                  |              |         X          |      X       |                     |                          |
| PostgreSQL 12+\[[3](#Ref_3)\] |            |                    |                                     |      X       |                    |      X       |          X          |                          |
| nginx                         |            |                    |                  X                  |              |                    |              |                     |                          |
| PAM                           |            |                    |                                     |              |                    |      X       |                     |                          |
| Liquibase 4                   |            |                    |                                     |      X       |                    |              |                     |                          |
| systemd                       |     X      |                    |                  X                  |              |                    |      X       |                     |            X             |
| PKCS \#11\[[2](#Ref_2)\]      |     X      |                    |                                     |              |                    |              |                     |                          |
| GNU Privacy Guard             |            |                    |                                     |              |                    |              |          X          |                          |
 
<a id="Ref_2" class="anchor"></a>
\[2\] The use of hardware cryptographic devices requires that a PKCS \#11 driver is installed and configured in the system.

<a id="Ref_3" class="anchor"></a>
\[3\] PostgreSQL version varies depending on operating system. By default, Ubuntu 20.04 uses 12, Ubuntu 22.04 - 14. User may also use external PostgreSQL server.

See [[ARC-CS]](#ARC-CS) for the Central Server details.