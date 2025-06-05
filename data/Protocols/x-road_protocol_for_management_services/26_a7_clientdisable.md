### A.7 clientDisable

Request message

```xml
--jetty1580127502lpv3owhr
Content-Type: text/xml; charset=UTF-8

<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header xmlns:ns4="http://x-road.eu/xsd/representation.xsd">
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>CLASS</id:memberClass>
            <id:memberCode>MEMBER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>BUSINESS</id:memberClass>
            <id:memberCode>servicemember2</id:memberCode>
            <id:serviceCode>clientDisable</id:serviceCode>
        </xroad:service>
        <xroad:id>4df02e1f-fc9b-4ae4-b61b-0dc1f7d28d1c</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientDisable>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>CLASS</id:memberClass>
                <id:memberCode>MEMBER</id:memberCode>
                <id:serverCode>SS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="SUBSYSTEM">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>CLASS</id:memberClass>
                <id:memberCode>MEMBER</id:memberCode>
                <id:subsystemCode>SUBSYSTEM</id:subsystemCode>
            </xroad:client>
        </xroad:clientDisable>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
--jetty1580127502lpv3owhr
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA

[OWNER SIGNATURE BYTES]
--jetty1580127502lpv3owhr
Content-Type: application/octet-stream

[OWNER CERTIFICATE BYTES]
--jetty1580127502lpv3owhr
Content-Type: application/octet-stream

[OWNER CERTIFICATE OCSP RESPONSE BYTES]
--jetty1580127502lpv3owhr--
```
Response message

```xml
<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:id="http://x-road.eu/xsd/identifiers" xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header xmlns:ns4="http://x-road.eu/xsd/representation.xsd">
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>CLASS</id:memberClass>
            <id:memberCode>MEMBER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>BUSINESS</id:memberClass>
            <id:memberCode>servicemember2</id:memberCode>
            <id:serviceCode>clientDisable</id:serviceCode>
        </xroad:service>
        <xroad:id>4df02e1f-fc9b-4ae4-b61b-0dc1f7d28d1c</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientDisableResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>CLASS</id:memberClass>
                <id:memberCode>MEMBER</id:memberCode>
                <id:serverCode>SS1</id:serverCode>
            </xroad:server>
            <xroad:client id:objectType="MEMBER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>CLASS</id:memberClass>
                <id:memberCode>MEMBER</id:memberCode>
            </xroad:client>
            <xroad:requestId>1122</xroad:requestId>
        </xroad:clientDisableResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```