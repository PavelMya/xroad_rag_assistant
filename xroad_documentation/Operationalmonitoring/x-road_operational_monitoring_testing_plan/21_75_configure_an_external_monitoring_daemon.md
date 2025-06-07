### 7.5 Configure an External Monitoring Daemon
Test case for verifying that it is possible to configure a secure connection between the security server and the external operational monitoring daemon.

**Preconditions:**
* The tester has superuser access to a server corresponding to the minimum requirements for an external monitoring daemon (see \[[UG-SS](#UG-SS)\]) to be used for installing an external operational monitoring daemon.

**Test scenario:**
* Install an external operational monitoring daemon according to the instructions in \[[UG-SS](#UG-SS)\].
* Configure security server *xtee10.ci.kit* to use the external operational monitoring daemon installed in the previous step over a secure connection. Follow the instructions in \[[UG-SS](#UG-SS)\].
* Send an X-Road request to a service provider in security server *xtee10.ci.kit*. The example request can be found in the source repository of the project at `src/systemtest/op-monitoring/requests/service_in_ss2.query` (the request endpoint is security server *xtee9.ci.kit*).
* Log in to the operational monitoring database in the external monitoring daemon (see [logging in to operational monitoring database](#log_in_db)) and ascertain that the operational monitoring data of the request sent in the previous step has been saved in the database. SQL example:
  ```sql
  SELECT * FROM operational_data WHERE message_id='abc';
  ```
* Send an operational data request to security server *xtee10.ci.kit*. Fill both 'recordsFrom' and 'recordsTo' value in with the 'monitoring_data_ts' value of the X-Road request that was sent to a service provider in security server xtee10.ci.kit. The example request can be found in the source repository of the project at `src/systemtest/op-monitoring/requests/operational_data_ss2.query`.

  **Expected output:** An operational data response is received. The operational data response contains the record of the X-Road request that was sent to a service provider in security server *xtee10.ci.kit*.
* Send a health data request to security server *xtee10.ci.kit*. The example request can be found in the source repository of the project at `src/systemtest/op-monitoring/requests/health_data_ss2.query`.

  **Expected output:** A health data response is received. The health data response contains the health data about the service that was queried in the first X-Road request as well as the health data about the service 'getSecurityServerOperationalData'.