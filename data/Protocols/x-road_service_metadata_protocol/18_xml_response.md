#### XML Response
`curl http://SECURITYSERVER/listClients`

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns2:clientList
        xmlns:ns1="http://x-road.eu/xsd/identifiers"
        xmlns:ns2="http://x-road.eu/xsd/xroad.xsd">
    <ns2:member>
        <ns2:id ns1:objectType="MEMBER">
            <ns1:xRoadInstance>AA</ns1:xRoadInstance>
            <ns1:memberClass>GOV</ns1:memberClass>
            <ns1:memberCode>TS1OWNER</ns1:memberCode>
        </ns2:id>
        <ns2:name>TS1 Owner</ns2:name>
    </ns2:member>
    <ns2:member>
        <ns2:id ns1:objectType="MEMBER">
            <ns1:xRoadInstance>AA</ns1:xRoadInstance>
            <ns1:memberClass>GOV</ns1:memberClass>
            <ns1:memberCode>TS2OWNER</ns1:memberCode>
        </ns2:id>
        <ns2:name>TS2 Owner</ns2:name>
    </ns2:member>
    <ns2:member>
        <ns2:id ns1:objectType="MEMBER">
            <ns1:xRoadInstance>AA</ns1:xRoadInstance>
            <ns1:memberClass>ENT</ns1:memberClass>
            <ns1:memberCode>CLIENT1</ns1:memberCode>
        </ns2:id>
        <ns2:name>Client One</ns2:name>
    </ns2:member>
    <ns2:member>
        <ns2:id ns1:objectType="SUBSYSTEM">
            <ns1:xRoadInstance>AA</ns1:xRoadInstance>
            <ns1:memberClass>ENT</ns1:memberClass>
            <ns1:memberCode>CLIENT1</ns1:memberCode>
            <ns1:subsystemCode>sub</ns1:subsystemCode>
        </ns2:id>
        <ns2:name>Client One</ns2:name>
        <ns2:subsystemName>Client One Sub</ns2:subsystemName>
    </ns2:member>
</ns2:clientList>
```