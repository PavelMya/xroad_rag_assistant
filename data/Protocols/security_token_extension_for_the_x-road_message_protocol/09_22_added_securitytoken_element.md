### 2.2 Added `securityToken` element
A new `securityToken` element was added to deliver the security token information.

```xml
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

```