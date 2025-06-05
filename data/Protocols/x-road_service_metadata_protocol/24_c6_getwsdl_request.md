### C.6 getWsdl Request
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xro="http://x-road.eu/xsd/xroad.xsd"
                  xmlns:iden="http://x-road.eu/xsd/identifiers">
    <soapenv:Header>
        <xro:protocolVersion>4.x</xro:protocolVersion>
        <xro:issue>123</xro:issue>
        <xro:id>123</xro:id>
        <xro:userId>123</xro:userId>
        <xro:service iden:objectType="SERVICE">
            <iden:xRoadInstance>FI</iden:xRoadInstance>
            <iden:memberClass>COM</iden:memberClass>
            <iden:memberCode>111</iden:memberCode>
            <iden:subsystemCode>SUB</iden:subsystemCode>
            <iden:serviceCode>getWsdl</iden:serviceCode>
            <iden:serviceVersion>v1</iden:serviceVersion>
        </xro:service>
        <xro:client iden:objectType="SUBSYSTEM">
            <iden:xRoadInstance>FI</iden:xRoadInstance>
            <iden:memberClass>COM</iden:memberClass>
            <iden:memberCode>111</iden:memberCode>
            <iden:subsystemCode>SUB</iden:subsystemCode>
        </xro:client>
    </soapenv:Header>
    <soapenv:Body>
        <xro:getWsdl>
            <xro:serviceCode>getRandom</xro:serviceCode>
            <xro:serviceVersion>v1</xro:serviceVersion>
        </xro:getWsdl>
    </soapenv:Body>
</soapenv:Envelope>
```