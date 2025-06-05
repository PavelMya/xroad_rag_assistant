## Annex C Example WSDL

```xml
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions targetNamespace="http://producer.x-road.eu"
        xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
        xmlns:tns="http://producer.x-road.eu"
        xmlns:xrd="http://x-road.eu/xsd/xroad.xsd"
        xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/"
        xmlns:xmime="http://www.w3.org/2005/05/xmlmime"
        xmlns:ref="http://ws-i.org/profiles/basic/1.1/xsd"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/">
    <wsdl:types>
        <xs:schema targetNamespace="http://producer.x-road.eu"
                xmlns:xs="http://www.w3.org/2001/XMLSchema">
            <xs:import namespace="http://x-road.eu/xsd/xroad.xsd"
                    schemaLocation="http://x-road.eu/xsd/xroad.xsd" />
            <xs:import namespace="http://ws-i.org/profiles/basic/1.1/xsd"
                    schemaLocation="http://ws-i.org/profiles/basic/1.1/swaref.xsd" />
            <xs:import namespace="http://www.w3.org/2005/05/xmlmime"
                    schemaLocation="http://www.w3.org/2005/05/xmlmime" />
            <xs:complexType name="fault">
                <xs:sequence>
                    <xs:element name="faultCode" type="xs:string">
                        <xs:annotation>
                            <xs:appinfo>
                                <xrd:title>Fault Code</xrd:title>
                            </xs:appinfo>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="faultString" type="xs:string">
                        <xs:annotation>
                            <xs:appinfo>
                                <xrd:title>Fault explanation</xrd:title>
                            </xs:appinfo>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
            <xs:element name="exampleService">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleInput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example input</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="exampleServiceResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleOutput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example output</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="fault" type="tns:fault"
                                minOccurs="0" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="exampleServiceSwaRef">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleInput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example input</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="exampleAttachment" type="ref:swaRef">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example Attachment (with swaRef
                                            description)</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="exampleServiceSwaRefResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleOutput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example output</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="fault" type="tns:fault"
                                minOccurs="0" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="exampleServiceMtom">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleInput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example input</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="exampleAttachment"
                                type="xs:base64Binary"
                                xmime:expectedContentTypes="application/octet-stream">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example MTOM
                                            Attachment</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="exampleServiceMtomResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="exampleOutput" type="xs:string">
                            <xs:annotation>
                                <xs:appinfo>
                                    <xrd:title>Example output</xrd:title>
                                </xs:appinfo>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="fault" type="tns:fault"
                                minOccurs="0" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:schema>
    </wsdl:types>

    <wsdl:message name="exampleService">
        <wsdl:part name="exampleService" element="tns:exampleService" />
    </wsdl:message>
    <wsdl:message name="exampleServiceResponse">
        <wsdl:part name="exampleServiceResponse"
                element="tns:exampleServiceResponse" />
    </wsdl:message>

    <wsdl:message name="exampleServiceSwaRef">
        <wsdl:part name="exampleServiceSwaRef"
                element="tns:exampleServiceSwaRef" />
    </wsdl:message>
    <wsdl:message name="exampleServiceSwaRefResponse">
        <wsdl:part name="exampleServiceSwaRefResponse"
                element="tns:exampleServiceSwaRefResponse" />
    </wsdl:message>

    <wsdl:message name="exampleServiceMtom">
        <wsdl:part name="exampleServiceMtom"
                element="tns:exampleServiceMtom" />
    </wsdl:message>
    <wsdl:message name="exampleServiceMtomResponse">
        <wsdl:part name="exampleServiceMtomResponse"
                element="tns:exampleServiceMtomResponse" />
    </wsdl:message>

    <wsdl:message name="requestHeader">
        <wsdl:part name="client" element="xrd:client" />
        <wsdl:part name="service" element="xrd:service" />
        <wsdl:part name="id" element="xrd:id" />
        <wsdl:part name="userId" element="xrd:userId" />
        <wsdl:part name="issue" element="xrd:issue" />
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion" />
    </wsdl:message>

    <wsdl:portType name="exampleServicePort">
        <wsdl:operation name="exampleService">
            <wsdl:documentation>
                <xrd:title>Title of exampleService</xrd:title>
                <xrd:notes>Technical notes for exampleService:
                        This is a simple SOAP service.</xrd:notes>
            </wsdl:documentation>
            <wsdl:input name="exampleService" message="tns:exampleService" />
            <wsdl:output name="exampleServiceResponse"
                    message="tns:exampleServiceResponse" />
        </wsdl:operation>

        <wsdl:operation name="exampleServiceSwaRef">
            <wsdl:documentation>
                <xrd:title>Title of exampleServiceSwaRef</xrd:title>
                <xrd:notes>Technical notes for exampleServiceSwaRef:
                        This is a SOAP service with
                        swaRef attachment.</xrd:notes>
            </wsdl:documentation>
            <wsdl:input name="exampleServiceSwaRef"
                    message="tns:exampleServiceSwaRef" />
            <wsdl:output name="exampleServiceSwaRefResponse"
                    message="tns:exampleServiceSwaRefResponse" />
        </wsdl:operation>

        <wsdl:operation name="exampleServiceMtom">
            <wsdl:documentation>
                <xrd:title>Title of exampleServiceMtom</xrd:title>
                <xrd:notes>Technical notes for exampleServiceMtom:
                        This is a SOAP service with
                        MTOM attachment.</xrd:notes>
            </wsdl:documentation>
            <wsdl:input name="exampleServiceMtom"
                    message="tns:exampleServiceMtom" />
            <wsdl:output name="exampleServiceMtomResponse"
                    message="tns:exampleServiceMtomResponse" />
        </wsdl:operation>
    </wsdl:portType>

    <wsdl:binding name="exampleServicePortSoap11"
            type="tns:exampleServicePort">
        <soap:binding style="document"
                transport="http://schemas.xmlsoap.org/soap/http" />
        <wsdl:operation name="exampleService">
            <soap:operation soapAction="" style="document" />
            <xrd:version>v1</xrd:version>
            <wsdl:input name="exampleService">
                <soap:body use="literal" />
                <soap:header message="tns:requestHeader"
                        part="client" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="service" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="id" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="userId" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="issue" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="protocolVersion" use="literal"/>
            </wsdl:input>
            <wsdl:output name="exampleServiceResponse">
                <soap:body use="literal" />
                <soap:header message="tns:requestHeader"
                        part="client" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="service" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="id" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="userId" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="issue" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="protocolVersion" use="literal" />
            </wsdl:output>
        </wsdl:operation>

        <wsdl:operation name="exampleServiceSwaRef">
            <soap:operation soapAction="" style="document" />
            <xrd:version>v1</xrd:version>
            <wsdl:input>
                <!-- MIME description is required according to WS-I Attachments
                     Profile Version 1.0: R2902 A SENDER MUST NOT send a
                     message using SOAP with Attachments if the corresponding
                     wsdl:input or wsdl:output element in the wsdl:binding does
                     not specify the WSDL MIME Binding.

                     The WSDL 1.1 specification does not specify whether the
                     soap:header element is permitted as a child of the
                     mime:part element along with the soap:body element. But
                     WS-I Attachments Profile Version 1.0 recommends including
                     both soap:header and soap:body as a content of mime:part.
                     However it should be noted that some tools like for
                     example SoapUI and Eclipse Web Services Explorer assume
                     that soap:header elements are children of wsdl:input or
                     wsdl:output elements. -->
                <mime:multipartRelated>
                    <mime:part>
                        <soap:body use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="client" use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="service" use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="id" use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="userId" use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="issue" use="literal" />
                        <soap:header message="tns:requestHeader"
                                part="protocolVersion" use="literal" />
                    </mime:part>
                </mime:multipartRelated>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
                <soap:header message="tns:requestHeader"
                        part="client" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="service" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="id" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="userId" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="issue" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="protocolVersion" use="literal" />
            </wsdl:output>
        </wsdl:operation>

        <wsdl:operation name="exampleServiceMtom">
            <soap:operation soapAction="" style="document" />
            <xrd:version>v1</xrd:version>
            <wsdl:input>
                <!-- MTOM does not require MIME description -->
                <soap:header message="tns:requestHeader"
                        part="client" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="service" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="id" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="userId" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="issue" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="protocolVersion" use="literal" />
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
                <soap:header message="tns:requestHeader"
                        part="client" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="service" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="id" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="userId" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="issue" use="literal" />
                <soap:header message="tns:requestHeader"
                        part="protocolVersion" use="literal" />
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="producerPortService">
        <wsdl:port name="exampleServicePortSoap11"
                binding="tns:exampleServicePortSoap11">
            <soap:address location="http://foo.bar.baz" />
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```