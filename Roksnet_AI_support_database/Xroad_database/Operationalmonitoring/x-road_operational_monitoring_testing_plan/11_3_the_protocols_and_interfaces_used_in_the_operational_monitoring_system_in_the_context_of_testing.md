## 3 The Protocols and Interfaces used in the Operational Monitoring System in the Context of Testing

The operational monitoring system supports the following protocols and interfaces:
* Store Operational Data (JSON)
* X-Road Message Protocol (SOAP, both regular X-Road messages and operational monitoring query requests)
* JMXMP interface for providing third-party monitoring systems (e.g. Zabbix) installed at security servers with health check data.

The JSON and SOAP-based interfaces are tested as part of the build-time unit tests as well as during automated integration testing. Within the set of unit tests, the focus is on low-level error handling, as opposed to the integration tests which focus on expected behavior in both successful and unsuccessful situations.

The JMXMP interface is tested manually.