#### 15.2.6 Monitoring Health Data over JMXMP

The operational monitoring daemon makes health data available over the JMXMP protocol. The Zabbix monitoring software can be configured to gather that data periodically, using its built in JMX interface type.

By default, the operational monitoring daemon JMXMP is disabled. JMXMP must be enabled for external tools such as Zabbix to be able to access the data. Please refer to the documentation at \[[JMX](#Ref_JMX)\] for instructions on configuring access to the JMX interface of the operational monitoring daemon.

For Zabbix to be able to gather data over JMX, the Zabbix Java gateway must be installed. See \[[ZABBIX-GATEWAY](#Ref_ZABBIX-GATEWAY)\] for instructions.

The JMX interface must be configured to each host item in Zabbix, for which health data needs to be obtained. See \[[ZABBIX-JMX](#Ref_ZABBIX-JMX)\] for instructions.

Please refer to \[[PR-OPMONJMX](#Ref_PR-OPMONJMX)\] for a specification of the names and attributes of the JMX objects exposed by the operational monitoring daemon.

The xroad-opmonitor package comes with sample host data that can be imported to Zabbix, containing a JMX interface, applications related to sample services and health data items under these services. Also, a script is provided for importing health data related applications and items to several hosts using the Zabbix API. Please find the example files in the directory `/usr/share/doc/xroad-opmonitor/examples/zabbix/`. Please refer to \[[ZABBIX-API](#Ref_ZABBIX-API)\] for information on the Zabbix API.

## 16 Environmental Monitoring

Environmental monitoring provides details of the Security Servers such as operating system, memory, disk space, CPU load, running processes and installed packages, etc.

### 16.1 Usage via SOAP API

Environmental monitoring provides SOAP API via X-Road message protocol extension. SOAP messages are described in \[[PR-ENVMONMES](#Ref_PR-ENVMONMES)\].

Monitoring extension schema is defined in \[[MONITORING_XSD](#Ref_MONITORING_XSD)\].