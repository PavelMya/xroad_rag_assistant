### 3.13 Operational Monitoring Protocol

This interface is used by external monitoring systems to gather operational information of the security server. The protocol is synchronous RPC style protocol that is initiated by the external monitoring system. The protocol is described in more detail in \[[PR-OPMON](#Ref_PR-OPMON)\].

### 3.14 Operational Monitoring JMX

This interface is used by a local monitoring system (e.g. Zabbix) to gather local operational health data of the security server via JMXMP. The interface is described in more detail in \[[ARC-OPMOND](#Ref_ARC-OPMOND)\] and \[[PR-OPMONJMX](#Ref_PR-OPMONJMX)\].

### 3.15 Environmental Monitoring Protocol

The environmental monitoring interface responds to queries for monitoring environmental data from security server's serverproxy interface. The environmental monitoring data is collected by environmental monitoring service.

### 3.16 Environmental Monitoring JMX

The environmental monitoring JMX service publishes environmental monitoring data via JMX interface. The environmental monitoring data is collected by environmental monitoring service.

### 3.17 Environmental Monitoring Query

The environmental monitoring query interface is used by the X-Road security server to retrieve environmental monitoring data from the environmental monitoring daemon.