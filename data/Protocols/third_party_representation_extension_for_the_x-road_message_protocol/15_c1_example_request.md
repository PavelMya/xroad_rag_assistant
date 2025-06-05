### C.1 Example Request

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
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:getRandom xmlns:ns1="http://v6Example.x-road.eu/producer">
            <amount>2</amount>
        </ns1:getRandom>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```