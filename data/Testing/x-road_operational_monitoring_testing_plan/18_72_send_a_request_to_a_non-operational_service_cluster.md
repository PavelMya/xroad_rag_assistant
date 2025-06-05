### 7.2 Send a Request to a Non-operational Service Cluster

Test case for verifying that the value of the operational monitoring data field 'service_security_server_address' in the operational monitoring database is null and that the request is marked as unsuccessful, in case an X-Road request is made to a non-operational service cluster. This test case is a supplement to the automated integration test [test_service_cluster](#test_service_cluster).

**Preconditions:**
* A two-node service cluster is configured in security servers *xtee8.ci.kit* and *xtee10.ci.kit*.
* A security server client of a third security server (*xtee9.ci.kit*) has an access right to the clustered service.

**Main scenario:**
* Stop the proxy in both security servers of the service cluster (`sudo service xroad-proxy stop`).
* Send an X-Road request from the service client in security server *xtee9.ci.kit* to the clustered service. The example request can be found in the source repository of the project at `src/systemtest/op-monitoring/requests/service_cluster.query`.
* Wait for the response - it takes up to 5 minutes before receiving a response stating that any target hosts could not be connected.

**Expected output:**
* There is an operational data record of the request in the operational monitoring database of the service client's security server.
* The value of the field 'succeeded' is false.
* The value of the field 'service_security_server_address' is null.