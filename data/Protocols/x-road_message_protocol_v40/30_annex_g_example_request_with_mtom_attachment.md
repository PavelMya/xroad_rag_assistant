## Annex G Example Request with MTOM Attachment

```xml
... other transport headers ... The following HTTP header is wrapped for readability:
Content-Type: multipart/related; type="application/xop+xml"; start="<rootpart>";
    start-info="text/xml"; boundary="MIME_boundary"
MIME-Version: 1.0

--MIME_boundary
Content-Type: application/xop+xml; charset=UTF-8; type="text/xml"
Content-Transfer-Encoding: 8bit
Content-ID: <rootpart>

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:ns1="http://producer.x-road.eu"
        xmlns:xrd="http://x-road.eu/xsd/xroad.xsd"
        xmlns:id="http://x-road.eu/xsd/identifiers">
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
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:exampleServiceMtom>
            <exampleInput>foo</exampleInput>
            <exampleAttachment>
                <inc:Include href="cid:data.bin"
                        xmlns:inc="http://www.w3.org/2004/08/xop/include" />
            </exampleAttachment>
        </ns1:exampleServiceMtom>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

--MIME_boundary
Content-Type: application/octet-stream; name=data.bin
Content-Transfer-Encoding: base64
Content-ID: <data.bin>
Content-Disposition: attachment; name="data.bin"; filename="data.bin"

VGhpcyBpcyBhdHRhY2htZW50Lg0K
--MIME_boundary--
```