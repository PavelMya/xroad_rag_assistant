## 2 Components of the Operational Monitoring System in the Context of Testing

The operational monitoring system involves the X-Road security server and the operational monitoring daemon. In addition, global configuration is obtained from the X-Road central server.

According to the architecture of the operational monitoring daemon (\[[ARC-OPMOND](#ARC-OPMOND)\]), the daemon is divided into the following components:
* operational monitoring database
* operational monitoring service

In the security server, the operational monitoring buffer is involved in forwarding operational data to the monitoring daemon.

In this project, testing will mainly focus on the behaviour of the operational monitoring daemon. The behavior of the operational monitoring buffer of the security server will be verified indirectly with integration testing, which involves X-Road message exchange, and will not be covered separately in this testing plan.