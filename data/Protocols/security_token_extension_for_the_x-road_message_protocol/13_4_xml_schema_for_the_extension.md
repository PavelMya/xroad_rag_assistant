## 4 XML Schema for the extension
The XML Schema for the extension is below. It can also be found at [`http://x-road.eu/xsd/security-token.xsd`](http://x-road.eu/xsd/security-token.xsd).
 ```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema elementFormDefault="qualified"
    targetNamespace="http://x-road.eu/xsd/security-token.xsd"
    xmlns="http://x-road.eu/xsd/security-token.xsd"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">

<!-- Header elements -->
<xs:element name="securityToken">
  <xs:complexType>
    <xs:simpleContent>
      <xs:restriction base="xs:string">
        <xs:attribute name="tokenType" type="xs:anyURI"/>
      </xs:restriction>
    </xs:simpleContent>
  </xs:complexType>
  <xs:annotation>
    <xs:documentation>Contains a security token</xs:documentation>
  </xs:annotation>
</xs:element>
</xs:schema>

```