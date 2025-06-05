## 14. Monitoring

Monitoring is taken to use by installing the monitoring support (see [IG-CS](#13-references) and appointing the central monitoring client as specified below.

Identity of central monitoring client (if any) is configured using Central Server's admin user interface. Configuration is done by updating a specific optional configuration file (see [UC-GCONF](#13-references)) monitoring-params.xml. This configuration file is distributed to all Security Servers through the global configuration distribution process (see [UC-GCONF](#13-references)).

```xml
<tns:conf xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:tns="http://x-road.eu/xsd/xroad.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://x-road.eu/xsd/xroad.xsd">
    <monitoringClient>
        <monitoringClientId id:objectType="SUBSYSTEM">
            <id:xRoadInstance>fdev</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>1710128-9</id:memberCode>
            <id:subsystemCode>LIPPIS</id:subsystemCode>
        </monitoringClientId>
    </monitoringClient>
</tns:conf>
```

One can configure either one member or a member's subsystem to be the central monitoring client. Permission to execute monitoring queries is strictly limited to that single member or subsystem - defining one subsystem to be a monitoring client does not grant the corresponding member access to querying monitoring data (and vice versa).

To disable central monitoring client altogether, update configuration to one which has no client:

```xml
<tns:conf xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:tns="http://x-road.eu/xsd/xroad.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://x-road.eu/xsd/xroad.xsd">
    <monitoringClient>
    </monitoringClient>
</tns:conf>
```