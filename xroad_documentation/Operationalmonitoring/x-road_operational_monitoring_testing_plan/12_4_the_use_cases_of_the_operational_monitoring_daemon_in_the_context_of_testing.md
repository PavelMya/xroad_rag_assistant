## 4 The Use Cases of the Operational Monitoring Daemon in the Context of Testing

The use cases defined in \[[UC-OPMON](#UC-OPMON)\] are directly or indirectly covered by the automated integration tests. In particular:
* UC OPMON_01: Storing operational data (and updating the in-memory health data) is carried out in all the automated test cases, unless the test checks that operational data is *not* written.
* UC OPMON_02: Querying operational data is carried out in all the automated test cases except for \[[test_health_data](#test_health_data)\] which only queries health data.
* UC OPMON_03: Health data of the security server is queried in the automated test case \[[test_health_data](#test_health_data)\].