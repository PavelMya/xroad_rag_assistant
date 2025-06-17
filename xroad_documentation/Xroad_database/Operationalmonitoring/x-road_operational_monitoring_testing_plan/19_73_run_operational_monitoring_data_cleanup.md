### 7.3 Run Operational Monitoring Data Cleanup

Test case for verifying that operational monitoring data is cleaned up periodically. The test can be executed in any of the operational monitoring daemon servers.

**Preconditions:**
* In the server where the test is executed, the default value has been set for system parameters *op-monitor.keep-records-for-days* and *op-monitor.clean-interval*.

**Main scenario:**
* Log in to operational monitoring database as user opmonitor, see [logging in to operational monitoring database.](#log_in_db)
* Count the records in the table `operational_data`:
   ```sql
   SELECT COUNT(*) FROM operational_data;
   ```
* The default value of the system parameter *op-monitor.keep-records-for-days* is 7 days. Operational data records that are older than one week will be deleted when data cleanup is run. Insert an operational data record with a timestamp from 2 weeks ago. SQL example:
   ```sql
   INSERT INTO operational_data(
       id, monitoring_data_ts, security_server_internal_ip,
       security_server_type, request_in_ts, response_out_ts, succeeded)
     VALUES (
       1,
       extract(epoch from (
         select date_trunc('day', NOW() - interval '2 weeks'))),
       '0.0.0.0', 'Client', 1, 1, 'f');
   ```
* The default value of the system parameter *op-monitor.clean-interval* is 12 hours. Add the following line to the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` to run data cleanup once a minute:
   ```
   clean-interval="0 0/1 * 1/1 * ? *"
   ```
* Restart the operational monitoring daemon (`sudo service xroad-opmonitor restart`).
* Wait for a minute for the data cleanup to run.

**Expected output:**
* The operational data record with a timestamp from 2 weeks ago has been deleted from the operational monitoring database.
* The number of records in the table `operational_data` is equal to the number of records before adding the record with a timestamp from 2 weeks ago.