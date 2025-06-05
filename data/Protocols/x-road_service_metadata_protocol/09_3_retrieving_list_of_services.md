## 3 Retrieving List of Services

X-Road provides two methods for getting the list of SOAP services offered by an X-Road client:

* `listMethods` lists all SOAP services offered by a service provider; and

* `allowedMethods` lists all SOAP services offered by a service provider that the caller has permission to invoke.

Both methods are invoked as regular X-Road SOAP services (see specification \[[PR-MESS](#Ref_PR-MESS)\] for details on the X-Road SOAP protocol). The connection type settings of the client subsystem is used when the methods are invoked.

The service SOAP header MUST contain the identifier of the target service provider and the value of the serviceCode element MUST be either `listMethods` or `allowedMethods`.
The body of the request MUST contain an appropriately named empty XML element (either `listMethods` or `allowedMethods`).
Annexes [C.3](#c3-listmethods-request) and [C.5](#c5-allowedmethods-request) contain example request messages for services, respectively.

The body of the response message MUST contain a list of services provided by the service provider (in case of listMethods) or open to the given client (in case of allowedMethods). The response SHALL NOT contain names of the metainfo services. The following snippet contains XML schema of the response body.
Annexes [C.4](#c4-listmethods-response) and [C.6](#c6-allowedmethods-response) contain example response messages for listMethods and allowedMethods services, respectively.
```xml
    <xs:element name="listMethodsResponse" type="MethodListType"/>
    <xs:element name="allowedMethodsResponse" type="MethodListType"/>

    <xs:complexType name="MethodListType">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0"
                name="service" type="id:XRoadServiceIdentifierType"/>
        </xs:sequence>
    </xs:complexType>
```