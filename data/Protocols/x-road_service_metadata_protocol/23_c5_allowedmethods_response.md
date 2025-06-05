### C.5 allowedMethods Response
```xml
<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xroad="http://x-road.eu/xsd/xroad.xsd"
        xmlns:id="http://x-road.eu/xsd/identifiers">
    <SOAP-ENV:Header>
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>Inst1</id:xRoadInstance>
            <id:memberClass>MemberClass1</id:memberClass>
            <id:memberCode>ClientId</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>Inst1</id:xRoadInstance>
            <id:memberClass>MemberClass1</id:memberClass>
            <id:memberCode>ProviderId</id:memberCode>
            <id:subsystemCode>Subsystem1</id:subsystemCode>
            <id:serviceCode>allowedMethods</id:serviceCode>
        </xroad:service>
        <xroad:id>411d6755661409fed365ad8135f8210be07613da</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
        <xroad:requestHash algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            TpY0dNunEru79Sp4mhqOirAiEWOhPXLOY5jDUib5HmF/
            3c5ayq2q44+0XJd49LsthLUq+2kI/Kp4/1ESuwr6Nw==
        </xroad:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:allowedMethodsResponse>
            <xroad:service id:objectType="SERVICE">
                <id:xRoadInstance>Inst1</id:xRoadInstance>
                <id:memberClass>MemberClass1</id:memberClass>
                <id:memberCode>ProviderId</id:memberCode>
                <id:subsystemCode>Subsystem1</id:subsystemCode>
                <id:serviceCode>allowedService</id:serviceCode>
                <id:serviceVersion>v1</id:serviceVersion>
            </xroad:service>
        </xroad:allowedMethodsResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```