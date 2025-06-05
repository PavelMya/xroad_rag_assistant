### A.2 clientDeletion

Request message

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:id="http://x-road.eu/xsd/identifiers"
        xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header>
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>clientDeletion</id:serviceCode>
        </xroad:service>
        <xroad:id>0e0d804a-b4e2-4f56-b5a0-2c32e4288f7d</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientDeletion>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="SUBSYSTEM">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>COM</id:memberClass>
                <id:memberCode>client</id:memberCode>
                <id:subsystemCode>subsystem</id:subsystemCode>
            </xroad:client>
        </xroad:clientDeletion>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Response message

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:id="http://x-road.eu/xsd/identifiers"
        xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header>
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>clientDeletion</id:serviceCode>
        </xroad:service>
        <xroad:id>0e0d804a-b4e2-4f56-b5a0-2c32e4288f7d</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
        <xroad:requestHash algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            KHe7PMAcYgNzcS7/4KImaYZxpLry0l+1zkFgzKXVkmzkYXg9IjBgX7CP6wDXwYT0qVON
            6NiF74LvlSwpPupO5A==
        </xroad:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientDeletionResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="SUBSYSTEM">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>COM</id:memberClass>
                <id:memberCode>client</id:memberCode>
                <id:subsystemCode>subsystem</id:subsystemCode>
            </xroad:client>
	     <xroad:requestId>395</xroad:requestId>
        </xroad:clientDeletionResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```