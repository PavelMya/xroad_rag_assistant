### 2.1 Identifiers

This section describes XML-based data formats for expressing the identifiers described informally in [Section 1.3](#13-identifying-entities). The data structures and elements defined in this section will be located under namespace `http://x-road.eu/xsd/identifiers`. The complete XML Schema is shown in [Annex A](#annex-a-xml-schema-for-identifiers).

The following listing shows the header of the schema definition.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
    elementFormDefault="qualified"
    targetNamespace="http://x-road.eu/xsd/identifiers"
    xmlns="http://x-road.eu/xsd/identifiers">
```

The `XRoadIdentifierType` complex type serves as the base for all other identifier types (derived by restriction). It contains a union of all fields that can be present in different identifiers. The attribute `objectType` contains the type of the identifier and can be used, for example, to distinguish between X-Road member and subsystem identifiers without resorting to conditions that check for presence of individual fields.

```xml
    <xs:complexType name="XRoadIdentifierType">
        <xs:sequence>
            <xs:element minOccurs="0" ref="xRoadInstance"/>
            <xs:element minOccurs="0" ref="memberClass"/>
            <xs:element minOccurs="0" ref="memberCode"/>
            <xs:element minOccurs="0" ref="subsystemCode"/>
            <xs:element minOccurs="0" ref="serviceCode"/>
            <xs:element minOccurs="0" ref="serviceVersion"/>
        </xs:sequence>
        <xs:attribute ref="objectType" use="required"/>
    </xs:complexType>
```

The enumeration `XRoadObjectType` lists all possible values of the `objectType` attribute.

```xml
    <xs:simpleType name="XRoadObjectType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="MEMBER"/>
            <xs:enumeration value="SUBSYSTEM"/>
            <xs:enumeration value="SERVICE"/>
        </xs:restriction>
    </xs:simpleType>
```

Next, we define elements and attributes used in the `XRoadIdentifierType`.

```xml
    <xs:element name="xRoadInstance" type="xs:string"/>
    <xs:element name="memberClass" type="xs:string"/>
    <xs:element name="memberCode" type="xs:string"/>
    <xs:element name="subsystemCode" type="xs:string"/>
    <xs:element name="serviceCode" type="xs:string"/>
    <xs:element name="serviceVersion" type="xs:string"/>
    <xs:attribute name="objectType" type="XRoadObjectType"/>
```

Finally, we define complex types for representing concrete types of identifiers. First, the `XRoadClientIdentifierType` is used to represent identifiers that can be used by the service clients, namely X-Road members and subsystems.

```xml
    <xs:complexType name="XRoadClientIdentifierType">
        <xs:complexContent>
            <xs:restriction base="XRoadIdentifierType">
                <xs:sequence>
                    <xs:element ref="xRoadInstance"/>
                    <xs:element ref="memberClass"/>
                    <xs:element ref="memberCode"/>
                    <xs:element minOccurs="0" ref="subsystemCode"/>
                </xs:sequence>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
```

The `XRoadServiceIdentifierType` can be used to represent identifiers of services.

```xml
    <xs:complexType name="XRoadServiceIdentifierType">
        <xs:complexContent>
            <xs:restriction base="XRoadIdentifierType">
                <xs:sequence>
                    <xs:element ref="xRoadInstance"/>
                    <xs:element ref="memberClass"/>
                    <xs:element ref="memberCode"/>
                    <xs:element minOccurs="0" ref="subsystemCode"/>
                    <xs:element ref="serviceCode"/>
                    <xs:element minOccurs="0" ref="serviceVersion"/>
                </xs:sequence>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
```