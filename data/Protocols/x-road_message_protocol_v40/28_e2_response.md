### E.2 Response

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:ns1="http://producer.x-road.eu"
        xmlns:id="http://x-road.eu/xsd/identifiers"
        xmlns:xrd="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header>
        <xrd:client id:objectType="SUBSYSTEM">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>MEMBER1</id:memberCode>
            <id:subsystemCode>SUBSYSTEM1</id:subsystemCode>
        </xrd:client>
        <xrd:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>MEMBER2</id:memberCode>
            <id:subsystemCode>SUBSYSTEM2</id:subsystemCode>
            <id:serviceCode>exampleService</id:serviceCode>
            <id:serviceVersion>v1</id:serviceVersion>
        </xrd:service>
        <xrd:id>4894e35d-bf0f-44a6-867a-8e51f1daa7e0</xrd:id>
        <xrd:userId>EE12345678901</xrd:userId>
        <xrd:issue>12345</xrd:issue>
        <xrd:protocolVersion>4.0</xrd:protocolVersion>
        <xrd:requestHash
                algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            29KTVbZf83XlfdYrsxjaSYMGoxvktnTUBTtA4BmSrh1e
            gtRtvR9VY8QycYaVdsKtGJIh/8CpucYWPbWfaIgJDQ==
        </xrd:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:exampleServiceResponse>
            <exampleOutput>bar</exampleOutput>
        </ns1:exampleServiceResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```