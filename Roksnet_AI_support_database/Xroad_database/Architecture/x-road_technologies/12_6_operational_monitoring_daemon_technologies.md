## 6 Operational monitoring daemon technologies

[Table 5](#Ref_Technology_matrix_of_the_operational_monitoring_daemon) presents the list of the technologies used in the operational monitoring daemon and the mapping between technologies and monitoring daemon components. 
Note: OP-monitoring daemon is an additional component of the X-Road.


Table 5. Technology matrix of the operational monitoring daemon

| Technology                    | Op. Mon.Daemon Main | Op. Mon.Database | Op. Mon.Service | ConfigurationClient |
|:------------------------------|:------------------------:|:---------------------:|:--------------------:|:------------------------:|
| Java 21                       |            X             |           X           |          X           |            X             |
| Logback                       |            X             |           X           |          X           |            X             |
| gRPC                          |            X             |           X           |                      |                          |
| PostgreSQL 12+\[[1](#Ref_1)\] |            X             |           X           |                      |                          |
| Liquibase 4                   |            X             |           X           |                      |                          |
| Dropwizard Metrics 4          |            X             |           X           |                      |                          |
| systemd                       |            X             |                       |                      |            X             |


\[1\] PostgreSQL version varies depending on operating system. By default, RHEL7 uses version 9, RHEL8 - 10,  RHEL9 - 13, Ubuntu 20.04 - 12, Ubuntu 22.04 - 14. User may also use external PostgreSQL server.


See [[ARC-OPMOND]](#ARC-OPMOND) for the operational monitoring daemon details.