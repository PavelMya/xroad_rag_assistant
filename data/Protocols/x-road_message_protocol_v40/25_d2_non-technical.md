### D.2 Non-technical

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
            <id:serviceCode>test</id:serviceCode>
            <id:serviceVersion>v1</id:serviceVersion>
        </xrd:service>
        <xrd:id>4894e35d-bf0f-44a6-867a-8e51f1daa7e0</xrd:id>
        <xrd:userId>EE12345678901</xrd:userId>
        <xrd:issue>12345</xrd:issue>
        <xrd:protocolVersion>4.0</xrd:protocolVersion>
        <xrd:requestHash
                algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            8r+UeXoU2WiEXRMdES8KBLhdQV/lt1DA+rLi2EUC239k
            OvBWGcBjYde27YIZtNQObsyHFQfX0V6pQ6LH3KS1Hw==
        </xrd:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:exampleServiceResponse>
            <exampleOutput />
            <fault>
                <faultCode>test_failed</faultCode>
                <faultString>Could not read test parameters</faultString>
            </fault>
        </ns1:exampleServiceResponse >
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```