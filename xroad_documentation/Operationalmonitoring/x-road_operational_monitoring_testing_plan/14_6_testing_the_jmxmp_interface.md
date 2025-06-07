## 6 Testing the JMXMP Interface

The JMXMP interface gets the data it exposes from the same component that is used to serve health data over the Operational Monitoring Query interface. Thus, the internal implementation of the health metrics registry is tested in the automated test case [test_health_data](#test_health_data). The main difference when directly using the JMXMP interface is in the format that the items are presented. The data exposed over JMXMP and their format are described in detail in \[[PR-OPMONJMX](#PR-OPMONJMX)\].

For quick reference, a couple of examples follow.

The keys of JMX items related to services are similar to this example:
  ```
  metrics:name=requestDuration(XTEE-CI-XM/GOV/00000001//getSecurityServerOperationalData)
  ```
where "//" represents a missing subsystem (the `getSecurityServerOperationalData` service is provided by the owner of the security server).

The keys of general JMX items are similar to this example:
  ```
  metrics:name=monitoringStartupTimestamp
  ```

During the project, the JMXMP interface will  be tested manually, using pre-configured Zabbix items in one or more Zabbix instances available in the testing environment, and using the `jconsole` application for directly observing the JMX metrics as they become available.

The configuration and usage of Zabbix is out of the scope of this document. The `jconsole` application is available in Java SDK-s, the installation of which is not in the scope of this document.

Direct observation of JMX metrics in `jconsole` is described in the following section.