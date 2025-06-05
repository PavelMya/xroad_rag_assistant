### 6.1 Testing the JMXMP Interface Using jconsole

By default, the JMX interface of the operational monitoring daemon is disabled. In order to conveniently access this interface from a remote host, either directly or through an SSH tunnel, the following configuration must be used in `/etc/xroad/services/local.properties`, effectively making changes on the `XROAD_OPMON_PARAMS` parameter value:

```bash
XROAD_OPMON_PARAMS=-Djava.rmi.server.hostname=<address> -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=<port> -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false
```

where `address` should be set to the desired listening address for access by `jconsole` and `port` should be set to the port number suitable for the system under test.

The health metrics of the operational monitoring daemon will appear on the `MBeans` tab, in the `metrics` subtree.

The items appearing under this subtree can be observed as the automated integration tests are run. Please refer to \[[PR-OPMONJMX](#PR-OPMONJMX)\] for the exact set of items required for each mediated request. Note that a separate `jconsole` session should be opened for the producer and the consumer security servers, to gain access to all the metrics made available.

**NOTE** Because the health metrics related to mediated services are reset upon each restart of the operational monitoring daemon, the necessary configuration of the system should be carried out before running each automated test case. Please refer to `src/systemtest/op-monitoring/integration/run_tests.py` (`LOCAL_INI_PARAMETERS` and each test case in `OperationalMonitoringIntegrationTest`) for information about the necessary configuration.