### A.5 ownerChange

Request message

```xml
--jetty113950090iemuz6a3
Content-Type: text/xml; charset=UTF-8
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
            <id:serviceCode>ownerChange</id:serviceCode>
        </xroad:service>
        <xroad:id>40c1a424-729d-4d52-bd77-ac6f70d1dac0</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:ownerChange>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="MEMBER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>COM</id:memberClass>
                <id:memberCode>MACK</id:memberCode>
            </xroad:client>
        </xroad:ownerChange>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
--jetty113950090iemuz6a3
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA
 
[NEW OWNER SIGNATURE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream
 
[NEW OWNER CERTIFICATE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream
 
[NEW OWNER CERTIFICATE OCSP RESPONSE BYTES]
--jetty113950090iemuz6a3--
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
            <id:serviceCode>ownerChange</id:serviceCode>
        </xroad:service>
        <xroad:id>40c1a424-729d-4d52-bd77-ac6f70d1dac0</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
        <xroad:requestHash
                algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            LGxmFNQhkhehCsbrrBgX4w64N0Z+knazghehKDYwJzSmVwf8tyVCYHyD8Vp5eSNNMtm0
            XDBzMOkqQ3uSDfNrLw==
        </xroad:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:ownerChangeResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="MEMBER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>COM</id:memberClass>
                <id:memberCode>MACK</id:memberCode>
            </xroad:client>
            <xroad:requestId>691</xroad:requestId>
        </xroad:ownerChangeResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```