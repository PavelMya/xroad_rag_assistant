### A.8 clientEnable

Request message

```xml
--jetty2041213627lpv3ox3x
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
            <id:serviceCode>clientEnable</id:serviceCode>
        </xroad:service>
        <xroad:id>0655793f-9adb-4e57-a0ec-6ea5bf69ce8a</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientEnable>
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
        </xroad:clientEnable>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
--jetty2041213627lpv3ox3x
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA

[OWNER SIGNATURE BYTES]
--jetty2041213627lpv3ox3x
Content-Type: application/octet-stream

[OWNER CERTIFICATE BYTES]
--jetty2041213627lpv3ox3x
Content-Type: application/octet-stream

[OWNER CERTIFICATE OCSP RESPONSE BYTES]
--jetty2041213627lpv3ox3x--

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
            <id:serviceCode>clientEnable</id:serviceCode>
        </xroad:service>
        <xroad:id>0655793f-9adb-4e57-a0ec-6ea5bf69ce8a</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:clientEnableResponse>
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
        </xroad:clientEnableResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```