### A.11 maintenanceModeDisable

Request message

```xml
--jetty832974847lp2nei0x
Content-Type: text/xml; charset=UTF-8
        
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header xmlns:ns4="http://x-road.eu/xsd/representation.xsd">
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>maintenanceModeDisable</id:serviceCode>
        </xroad:service>
        <xroad:id>7f47514b-a6eb-40ce-afea-34e81d7b38a3</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:maintenanceModeDisable>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
        </xroad:maintenanceModeDisable>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
--jetty832974847lp2nei0x
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA

[OWNER SIGNATURE BYTES]
--jetty832974847lp2nei0x
Content-Type: application/octet-stream

[OWNER CERTIFICATE BYTES]
--jetty832974847lp2nei0x
Content-Type: application/octet-stream

[OWNER CERTIFICATE OCSP RESPONSE BYTES]
--jetty832974847lp2nei0x--
```

Response message

```xml
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header xmlns:ns4="http://x-road.eu/xsd/representation.xsd">
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>maintenanceModeDisable</id:serviceCode>
        </xroad:service>
        <xroad:id>7f47514b-a6eb-40ce-afea-34e81d7b38a3</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:maintenanceModeDisableResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:requestId>1133</xroad:requestId>
        </xroad:maintenanceModeDisableResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```