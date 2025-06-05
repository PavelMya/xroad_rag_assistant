### 2.1 *clientReg* - Security Server Client Registration

The client registration service is invoked by the Security Server when a new client is added to the server.

The body of the client registration message (request or response) contains the following fields:

* **client** – identifier of the subsystem to be added to the Security Server;

* **subsystemName** – optional new name of the subsystem if client is subsystem;

* **server** – identifier of the Security Server where the client is added;

* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the client registration request body is shown below. For clarity, documentation in the schema fragment is omitted.

```xml
<xsd:complexType name="ClientRequestType">
    <xsd:sequence>
        <xsd:element name="server" type="id:XRoadSecurityServerIdentifierType"/>
        <xsd:element name="client" type="id:XRoadClientIdentifierType"/>
        <xsd:element name="subsystemName" type="string" minOccurs="0" />
        <element name="requestId" type="tns:RequestIdType" minOccurs="0"/>
    </xsd:sequence>
</xsd:complexType>
```

The request is sent using HTTP POST method. The content type of the request MUST be *multipart/related* and the request must contain the following MIME parts.

1. X-Road SOAP request message. The message MUST contain the regular X-Road headers and the two data fields (*server*, *client*). The content type of this part MUST be *text/xml*.

2. Signature of the member that owns the subsystem to be registered as a Security Server client. The MIME part must contain signature of the SOAP request message, created with the private key corresponding to a **signing certificate** of the subsystem's owner. The content type of this part must be *application/octet-stream*. Additionally, the part MUST include header field *signature-algorithm-ID* that identifies the signature algorithm. Currently supported signature algorithms are *SHA256withRSA*, *SHA384withRSA*, *SHA512withRSA*, *SHA256withRSAandMGF1*, *SHA384withRSAandMGF1*, and *SHA512withRSAandMGF1*.

3. Signing certificate of the subsystem's owner that was used to create the second MIME part. The content type of this part MUST be *application/octet-stream*.

4. OCSP response certifying that the signing certificate was valid at the time of creation of the request. The content type of this part MUST be *application/octet-stream*.

The response echoes back the subsystemName, the client and the server fields of the request and adds the field *requestId*.

An example of the client registration request and response is given in [Annex A.1](#a1-clientreg).