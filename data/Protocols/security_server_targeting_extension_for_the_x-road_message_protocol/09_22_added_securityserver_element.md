### 2.2 Added `securityServer` element
A new `securityServer` element was added to identify the specific target security server.

```xml
 <xs:element name="securityServer" type="id:XRoadSecurityServerIdentifierType">
        <xs:annotation>
            <xs:documentation>Identifies a specific security server</xs:documentation>
        </xs:annotation>
    </xs:element>
```
  The element is of the type `XRoadSecurityServerIdentifierType`, which is one of the identifiers already defined
  in the X-Road Message Protocol v 4.0 \[[PR-MESS](#Ref_PR-MESS)\] section 2.1. The whole XML schema for the identifier types is defined in
  Annex A of the same document. The relevant part is listed below for convenience.

```xml
<xs:complexType name="XRoadSecurityServerIdentifierType">
    <xs:complexContent>
        <xs:restriction base="XRoadIdentifierType">
            <x:sequence>
                <xs:element ref="xRoadInstance"/>
                <xs:element ref="memberClass"/>
                <xs:element ref="memberCode"/>
                <xs:element ref="serverCode"/>
            </xs:sequence>
            <xs:attribute ref="objectType" use="required" fixed="SERVER"/>
        </xs:restriction>
    </xs:complexContent>
</xs:complexType>
```