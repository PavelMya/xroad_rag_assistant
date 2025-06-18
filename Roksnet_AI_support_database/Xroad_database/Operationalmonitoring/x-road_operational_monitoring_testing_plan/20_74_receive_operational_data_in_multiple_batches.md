### 7.4 Receive Operational Data in Multiple Batches

Test case for verifying that in case the amount of relevant operational data records exceeds the value of the *op-monitor.max-records-in-payload* system parameter, the operational data is returned in correct batches and the value of 'nextRecordsFrom' element in the operational data response is correct. This test case is a supplement to the automated integration test [ test_limited_operational_data_response](#test_limited_operational_data_response).

**Background:**

While composing the operational data response, the number of records allowed in maximum payload plus all records that have the same timestamp as the last included record are included in the response. Therefore more records than specified by the system parameter *op-monitor.max-records-in-payload* can be included in the response in case there is more than one record with the same timestamp as the last included record in the operational monitoring database. The element 'nextRecordsFrom' is present in the operational data response only in case the result of the query includes more records than the defined maximum number of records in the response allows.

**Preconditions:**
* In security server *xtee9.ci.kit* the value of the system parameter *op-monitor.records-available-timestamp-offset-seconds* has been set to 0 to avoid the presence of 'nextRecordsFrom' element in the operational data response due to long offset period.

**Main scenario:**

All test steps are executed in security server *xtee9.ci.kit*.
* The default value of the system parameter *op-monitor.max-records-in-payload* is 10,000. To limit the maximum number of records in payload to 1, add the following line to the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini`:
   ```
   max-records-in-payload=1
   ```
* Restart the operational monitoring daemon (`sudo service xroad-opmonitor restart`).
* It is necessary to populate the operational monitoring database with some data suitable for testing. To do that, send the following requests to security server *xtee9.ci.kit*:
  * send an X-Road request;
  * wait for a couple of seconds;
  * send an operational data request;
  * wait for a couple of seconds;
  * send another X-Road request;

 The example requests can be found in the source repository of the project at `src/systemtest/op-monitoring/requests`. Use `simple.query` for an X-Road request and `operational_data.query` for an operational data request.
* Log in to the operational monitoring database (see [logging in to operational monitoring database](#log_in_db)) and view the timestamps of the most recent operational data records. SQL example:
   ```sql
   SELECT monitoring_data_ts, message_id, service_code, security_server_type
   FROM operational_data
   ORDER BY monitoring_data_ts
   DESC LIMIT 5;
   ```
* Make sure that the value of 'monitoring_data_ts' is unique in case of X-Road request records, and equal in case of operational data records for both the client and producer roles. Send the operational data requests to security server *xtee9.ci.kit* with the following 'recordsFrom' and 'recordsTo' values and expecting the following responses.

  1. Fill both 'recordsFrom' and 'recordsTo' value with the 'monitoring_data_ts' value of the first X-Road request in the database.

   **Expected output**: There is one operational data record in the operational data response: the record of the first X-Road request. The element 'nextRecordsFrom' is not present in the response.
  2. Fill both 'recordsFrom' and 'recordsTo' value with the 'monitoring_data_ts' value of the operational data request records in the database.

   **Expected output**: There are 2 operational data records in the operational data response: the client and producer side records of the operational data request. The element 'nextRecordsFrom' is not present in the response.
  3. Fill the 'recordsFrom' value in with the 'monitoring_data_ts' value of the first X-Road request in the database. Fill the 'recordsTo' value in with the 'monitoring_data_ts' value of the operational data request records in the database.

   **Expected output**: There is one operational data record in the operational data response: the record of the first X-Road request. The element 'nextRecordsFrom' is present in the response. The value of the element 'nextRecordsFrom' is (the value of 'monitoring_data_ts' of the first X-Road request + 1).
  4. Fill the 'recordsFrom' value in with the 'monitoring_data_ts' value of the operational data request records in the database. Fill the 'recordsTo' value in with the 'monitoring_data_ts' value of the second X-Road request in the database.

   **Expected output**: There are 2 operational data records in the operational data response: the client and producer side records of the operational data request. The element 'nextRecordsFrom' is present in the response. The value of the element 'nextRecordsFrom' is (the value of 'monitoring_data_ts' of the operational data request records + 1).