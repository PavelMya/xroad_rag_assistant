### 7.1 Test Helpers
The test steps described here are to be executed when refered to in test cases.
* <a name="log_in_db"></a>**Logging in to operational monitoring database as user opmonitor**: In the server running the operational monitoring daemon, enter the command
   ```bash
   psql -h 127.0.0.1 -U opmonitor op-monitor
   ```

   The password for user opmonitor can be found in `/etc/xroad/db.properties`.