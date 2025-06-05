### WSDL
```xml
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions targetNamespace="http://x-road.eu/xsd/xroad.xsd"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xrd="http://x-road.eu/xsd/xroad.xsd"
    xmlns:id="http://x-road.eu/xsd/identifiers"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/">
    <wsdl:types>
        <xs:schema targetNamespace="http://x-road.eu/xsd/xroad.xsd" elementFormDefault="qualified">
            <xs:include schemaLocation="http://x-road.eu/xsd/xroad.xsd" />
            <xs:import namespace="http://x-road.eu/xsd/identifiers"
                schemaLocation="http://x-road.eu/xsd/identifiers.xsd"/>

            <xs:element name="listMethods">
                <xs:complexType>
                    <xs:sequence />
                </xs:complexType>
            </xs:element>
            <xs:element name="allowedMethods">
                <xs:complexType>
                    <xs:sequence />
                </xs:complexType>
            </xs:element>
            <xs:element name="listMethodsResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element maxOccurs="unbounded" minOccurs="0" name="service"
                            type="id:XRoadServiceIdentifierType" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="allowedMethodsResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element maxOccurs="unbounded" minOccurs="0" name="service"
                            type="id:XRoadServiceIdentifierType" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="getWsdl">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="serviceCode" type="xs:string"/>
                        <xs:element name="serviceVersion" type="xs:string" minOccurs="0"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="getWsdlResponse">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="serviceCode" type="xs:string"/>
                        <xs:element name="serviceVersion" type="xs:string" minOccurs="0"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:schema>
    </wsdl:types>

    <wsdl:message name="listMethods">
            <wsdl:part name="listMethods" element="xrd:listMethods"/>

            <wsdl:part name="client" element="xrd:client"/>
            <wsdl:part name="service" element="xrd:service"/>
            <wsdl:part name="userId" element="xrd:userId"/>
            <wsdl:part name="id" element="xrd:id"/>
            <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
     </wsdl:message>

    <wsdl:message name="listMethodsResponse">
        <wsdl:part name="listMethodsResponse" element="xrd:listMethodsResponse"/>

        <wsdl:part name="client" element="xrd:client"/>
        <wsdl:part name="service" element="xrd:service"/>
        <wsdl:part name="userId" element="xrd:userId"/>
        <wsdl:part name="id" element="xrd:id"/>
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
    </wsdl:message>

    <wsdl:message name="allowedMethods">
        <wsdl:part name="allowedMethods" element="xrd:allowedMethods"/>

        <wsdl:part name="client" element="xrd:client"/>
        <wsdl:part name="service" element="xrd:service"/>
        <wsdl:part name="userId" element="xrd:userId"/>
        <wsdl:part name="id" element="xrd:id"/>
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
    </wsdl:message>

    <wsdl:message name="allowedMethodsResponse">
        <wsdl:part name="allowedMethodsResponse" element="xrd:allowedMethodsResponse"/>

        <wsdl:part name="client" element="xrd:client"/>
        <wsdl:part name="service" element="xrd:service"/>
        <wsdl:part name="userId" element="xrd:userId"/>
        <wsdl:part name="id" element="xrd:id"/>
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
    </wsdl:message>

    <wsdl:message name="getWsdl">
        <wsdl:part name="getWsdl" element="xrd:getWsdl"/>

        <wsdl:part name="client" element="xrd:client"/>
        <wsdl:part name="service" element="xrd:service"/>
        <wsdl:part name="userId" element="xrd:userId"/>
        <wsdl:part name="id" element="xrd:id"/>
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
    </wsdl:message>

    <wsdl:message name="getWsdlResponse">
        <wsdl:part name="getWsdlResponse" element="xrd:getWsdlResponse"/>
        <!-- the wsdl is returned as an attachment -->
        <wsdl:part name="wsdl" type="xs:base64Binary"/>

        <wsdl:part name="client" element="xrd:client"/>
        <wsdl:part name="service" element="xrd:service"/>
        <wsdl:part name="userId" element="xrd:userId"/>
        <wsdl:part name="id" element="xrd:id"/>
        <wsdl:part name="protocolVersion" element="xrd:protocolVersion"/>
    </wsdl:message>

    <wsdl:portType name="metaServicesPort">
        <wsdl:operation name="allowedMethods">
            <wsdl:documentation>
                <xrd:title>allowedMethods</xrd:title>
            </wsdl:documentation>
            <wsdl:input name="allowedMethods" message="xrd:allowedMethods"/>
            <wsdl:output name="allowedMethodsResponse" message="xrd:allowedMethodsResponse"/>
        </wsdl:operation>
        <wsdl:operation name="listMethods">
            <wsdl:documentation>
                <xrd:title>listMethods</xrd:title>
            </wsdl:documentation>
            <wsdl:input name="listMethods" message="xrd:listMethods"/>
            <wsdl:output name="listMethodsResponse" message="xrd:listMethodsResponse"/>
        </wsdl:operation>
        <wsdl:operation name="getWsdl">
            <wsdl:input message="xrd:getWsdl" name="getWsdl"/>
            <wsdl:output message="xrd:getWsdlResponse" name="getWsdlResponse"/>
        </wsdl:operation>
    </wsdl:portType>

    <wsdl:binding name="metaServicesPortSoap11" type="xrd:metaServicesPort">
        <soap:binding style="document"
                      transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="allowedMethods">
            <soap:operation soapAction=""/>
            <wsdl:input name="allowedMethods">
                <soap:body parts="allowedMethods" use="literal"/>
                <soap:header message="xrd:allowedMethods" part="client" use="literal"/>
                <soap:header message="xrd:allowedMethods" part="service" use="literal"/>
                <soap:header message="xrd:allowedMethods" part="userId" use="literal"/>
                <soap:header message="xrd:allowedMethods" part="id" use="literal"/>
                <soap:header message="xrd:allowedMethods" part="protocolVersion" use="literal"/>
            </wsdl:input>
            <wsdl:output name="allowedMethodsResponse">
                <soap:body parts="allowedMethodsResponse" use="literal"/>
                <soap:header message="xrd:allowedMethodsResponse" part="client" use="literal"/>
                <soap:header message="xrd:allowedMethodsResponse" part="service" use="literal"/>
                <soap:header message="xrd:allowedMethodsResponse" part="userId" use="literal"/>
                <soap:header message="xrd:allowedMethodsResponse" part="id" use="literal"/>
                <soap:header message="xrd:allowedMethodsResponse" part="protocolVersion" use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="listMethods">
            <soap:operation soapAction=""/>
            <wsdl:input name="listMethods">
                <soap:body parts="listMethods" use="literal"/>
                <soap:header message="xrd:listMethods" part="client" use="literal"/>
                <soap:header message="xrd:listMethods" part="service" use="literal"/>
                <soap:header message="xrd:listMethods" part="userId" use="literal"/>
                <soap:header message="xrd:listMethods" part="id" use="literal"/>
                <soap:header message="xrd:listMethods" part="protocolVersion" use="literal"/>
            </wsdl:input>
            <wsdl:output name="listMethodsResponse">
                <soap:body parts="listMethodsResponse" use="literal"/>
                <soap:header message="xrd:listMethodsResponse" part="client" use="literal"/>
                <soap:header message="xrd:listMethodsResponse" part="service" use="literal"/>
                <soap:header message="xrd:listMethodsResponse" part="userId" use="literal"/>
                <soap:header message="xrd:listMethodsResponse" part="id" use="literal"/>
                <soap:header message="xrd:listMethodsResponse" part="protocolVersion" use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="getWsdl">
            <soap:operation soapAction=""/>
            <wsdl:input name="getWsdl">
                <soap:body parts="getWsdl" use="literal"/>
                <soap:header message="xrd:getWsdl" part="client" use="literal"/>
                <soap:header message="xrd:getWsdl" part="service" use="literal"/>
                <soap:header message="xrd:getWsdl" part="userId" use="literal"/>
                <soap:header message="xrd:getWsdl" part="id" use="literal"/>
                <soap:header message="xrd:getWsdl" part="protocolVersion" use="literal"/>
            </wsdl:input>
            <wsdl:output name="getWsdlResponse">
                <mime:multipartRelated>
                    <mime:part>
                        <soap:body parts="getWsdlResponse" use="literal"/>
                        <soap:header message="xrd:getWsdlResponse" part="client" use="literal"/>
                        <soap:header message="xrd:getWsdlResponse" part="service" use="literal"/>
                        <soap:header message="xrd:getWsdlResponse" part="userId" use="literal"/>
                        <soap:header message="xrd:getWsdlResponse" part="id" use="literal"/>
                        <soap:header message="xrd:getWsdlResponse" part="protocolVersion" use="literal"/>
                    </mime:part>
                    <mime:part>
                        <mime:content part="wsdl" type="text/xml"/>
                    </mime:part>
                </mime:multipartRelated>
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>

    <wsdl:service name="producerPortService">
        <wsdl:port name="metaServicesPortSoap11"
            binding="xrd:metaServicesPortSoap11">
            <soap:address location="https://SECURITYSERVER/" />
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```