### C.7 getWsdl Response
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:iden="http://x-road.eu/xsd/identifiers"
                  xmlns:xro="http://x-road.eu/xsd/xroad.xsd">
    <soapenv:Header>
        <xro:protocolVersion>4.x</xro:protocolVersion>
        <xro:issue>123</xro:issue>
        <xro:id>123</xro:id>
        <xro:requestHash algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            BPiSSkxGzJC4piyVjkTRfNRROHI/hQJc1rALJsPAvghMUM0keBXV6QKVIUJPUjDydw2+wadRUkM6MS8vO3Y88w==
        </xro:requestHash>
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
        <xro:getWsdlResponse>
            <xro:serviceCode>getRandom</xro:serviceCode>
            <xro:serviceVersion>v1</xro:serviceVersion>
        </xro:getWsdlResponse>
    </soapenv:Body>
</soapenv:Envelope>
```