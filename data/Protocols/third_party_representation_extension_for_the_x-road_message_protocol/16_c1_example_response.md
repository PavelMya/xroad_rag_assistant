### C.1 Example Response

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xrd="http://x-road.eu/xsd/xroad.xsd" 
    xmlns:id="http://x-road.eu/xsd/identifiers" 
    xmlns:repr="http://x-road.eu/xsd/representation.xsd">
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
            <id:serviceCode>getRandom</id:serviceCode>
            <id:serviceVersion>v1</id:serviceVersion>
        </xrd:service>
        <repr:representedParty>
            <repr:partyClass>COM</repr:partyClass>
            <repr:partyCode>MEMBER3</repr:partyCode>
        </repr:representedParty>
        <xrd:userId>EE1234567890</xrd:userId>
        <xrd:id>4894e35d-bf0f-44a6-867a-8e51f1daa7e0</xrd:id>
        <xrd:protocolVersion>4.0</xrd:protocolVersion>
        <xrd:requestHash algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">WJGPAGv7 AebB+yhYgYjkqzsSOjCMf+kvDmMVvq0RiLOyjm8IVxxI1aB31OJG+SoYyv AngBYqP34Pt1CjJ4nTJQ==</xrd:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xxprod:getRandomResponse xmlns:xxprod="http://v6Example.x-road.eu/producer">
            <randomValues>
                <randomValue>0.123456789</randomValue>
                <randomValue>0.987654321</randomValue>
            </randomValues>
        </xxprod:getRandomResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```