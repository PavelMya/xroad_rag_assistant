## 5 Automated Integration Testing in Detail

Automated integration tests are carried out on a pre-configured testing system with the required X-Road components installed and configured, as described in \[[TEST-OPMONSTRAT](#TEST-OPMONSTRAT)\]. It is assumed that during integration testing, no manual testing is carried out on the same systems. Otherwise, arbitrary X-Road message exchange would interfere with the tests and cause false negative results.

The testcases are listed in alphabetical order. They can be run in an arbitrary order and do not depend on the results of each other.

**NOTE** The test cases require specific values for some configuration parameters of the security servers or the operational monitoring daemon. If such values are not present, the services are reconfigured and restarted automatically. After each test case, the initial configuration is restored, and the services are restarted.

The test scripts and their input files can be found in the source repository of the project at `src/systemtest/op-monitoring/xrd-opmon-tests`. Please refer to `src/systemtest/op-monitoring/xrd-opmon-tests/README.md` for instructions on running the tests.

The following test cases have been automated at integration testing level:
1. `test_attachments`, verifying that information about attachments in X-Road requests and responses is stored and returned as required.
2. `test_client_filter`, verifying the access rights to monitoring data of various types of clients (the owner of the security server, the central monitoring client and regular clients).
3. `test_get_metadata`, verifying that information about HTTP GET metadata requests (getWsdl, listClients, verificationconf) is stored (or not) and returned (or not) as required.
4. <a name="test_health_data"></a>`test_health_data`, verifying that correct health data is returned for each service for which X-Road requests are handled.
5. <a name="test_limited_operational_data_response"></a>`test_limited_operational_data_response`, verifying that returning operational data in batches (depending on the configuration) works as required.
6. `test_metaservices`, verifying that information about metaservice requests (listMethods, getSecurityServerMetrics) is stored and returned as required.
7. `test_outputspec`, verifying that the set of fields present in operational data responses can be provided in operational data requests and that the responses are consistent with this set of fields.
8. <a name="test_service_cluster"></a>`test_service_cluster`, verifying that information about requests to services that are in a cluster, is stored and returned as required.
9. `test_simple_store_and_query`, verifying that operational data is stored about regular X-Road requests as well as operational data requests themselves.
10. `test_soap_fault`, verifying that information about requests resulting in SOAP faults at various points in the request exchange chain, is stored and returned as required.
11. `test_zero_buffer_size`, verifying that in case the operational monitoring buffer size has been set to zero, the operational monitoring data of X-Road requests is not stored by the operational monitoring daemon and can't be queried.
12. `test_time_interval`, verifying that operational data can be queried about specific time intervals as required, and that errors are handled as required.