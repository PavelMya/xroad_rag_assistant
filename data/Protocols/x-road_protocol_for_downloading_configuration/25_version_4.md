### Version 4

- Changes in version 4:
    - optional *authenticationCertificateProfileId* element of type *string* was added into *AcmeServer* to improve some ACME server's certificate ordering process.
    - optional *signingCertificateProfileId* element of type *string* was added into *AcmeServer* to improve some ACME server's certificate ordering process.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
        xmlns:tns="http://x-road.eu/xsd/xroad.xsd"
        targetNamespace="http://x-road.eu/xsd/xroad.xsd"
        xmlns:id="http://x-road.eu/xsd/identifiers">
    <import namespace="http://x-road.eu/xsd/identifiers"
            schemaLocation="http://x-road.eu/xsd/identifiers.xsd" id="id"/>

    <element name="conf" type="tns:SharedParametersType">
        <annotation>
            <documentation>Set of configuration parameters that are
                used by members of this X-Road instance and other
                federated instances.
            </documentation>
        </annotation>
    </element>

    <complexType name="SharedParametersType">
        <sequence>
            <element name="instanceIdentifier" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies this
                        instance of the X-Road system within a
                        federation of systems.
                    </documentation>
                </annotation>
            </element>
            <element name="source" type="tns:ConfigurationSourceType" maxOccurs="unbounded">
                <annotation>
                    <documentation>Describes one configuration source.
                    </documentation>
                </annotation>
            </element>
            <element name="approvedCA" type="tns:ApprovedCAType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Certification authority approved
                        by the Governing Authority of providing
                        certification services for members of this
                        X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="approvedTSA" type="tns:ApprovedTSAType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Time-stamping authority approved
                        by the Governing Authority of providing
                        time-stamping services for members of this
                        X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="member" type="tns:MemberType" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>Registered member of this X-Road
                        system.
                    </documentation>
                </annotation>
            </element>
            <element name="securityServer"
                     type="tns:SecurityServerType" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>Security server registered in this
                        X-Road system.
                    </documentation>
                </annotation>
            </element>
            <element name="globalGroup" type="tns:GlobalGroupType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Group of access rights subjects,
                        defined by the Governing Authority. An access
                        rights subject can be either a member or a
                        subsystem.
                    </documentation>
                </annotation>
            </element>
            <element name="centralService"
                     type="tns:CentralServiceType" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>Central service, defined by the
                        Governing Authority.
                    </documentation>
                </annotation>
            </element>
            <element name="globalSettings"
                     type="tns:GlobalSettingsType">
                <annotation>
                    <documentation>Classifiers and security policy
                        settings used in this X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <any processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
    </complexType>

    <complexType name="ConfigurationSourceType">
        <sequence>
            <element name="address" type="string">
                <annotation>
                    <documentation>The address of the central server which provides the signed configuration.</documentation>
                </annotation>
            </element>
            <element name="internalVerificationCert" type="base64Binary" maxOccurs="unbounded">
                <annotation>
                    <documentation>Public key that can be used to verify the signed configuration, presented as X.509 certificate.</documentation>
                </annotation>
            </element>
            <element name="externalVerificationCert" type="base64Binary" maxOccurs="unbounded">
                <annotation>
                    <documentation>Public key that can be used to verify the signed configuration, presented as X.509 certificate.</documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="MemberType">
        <sequence>
            <element name="memberClass" type="tns:MemberClassType">
                <annotation>
                    <documentation>Member class of the member.
                    </documentation>
                </annotation>
            </element>
            <element name="memberCode" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies the
                        member within the given member class.
                    </documentation>
                </annotation>
            </element>
            <element name="name" type="string">
                <annotation>
                    <documentation>Full, official name of the member,
                        used in user interfaces.
                    </documentation>
                </annotation>
            </element>
            <element name="subsystem" type="tns:SubsystemType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Represents information about a
                        part of the member's information system that
                        is acting as an independent service consumer
                        or provider in the X-Road system.
                    </documentation>
                </annotation>
            </element>
        </sequence>
        <attribute name="id" type="ID"/>
    </complexType>

    <complexType name="SecurityServerType">
        <sequence>
            <element name="owner" type="IDREF">
                <annotation>
                    <documentation>Identifier of the member who is
                        responsible for the security server.
                    </documentation>
                </annotation>
            </element>
            <element name="serverCode" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies this
                        server within servers owned by the same
                        member.
                    </documentation>
                </annotation>
            </element>
            <element name="address" type="string" minOccurs="0">
                <annotation>
                    <documentation>Externally visible address of the
                        security server.
                    </documentation>
                </annotation>
            </element>
            <element name="authCertHash" type="base64Binary"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Hash of the authentication
                        certificate used by the security server.
                    </documentation>
                </annotation>
            </element>
            <element name="client" type="IDREF" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>Identifier a registered client of
                        this security server. Client can be either a
                        member or a subsystem.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="ApprovedCAType">
        <sequence>
            <element name="name" type="string">
                <annotation>
                    <documentation>Name of the CA, used in user
                        interfaces.
                    </documentation>
                </annotation>
            </element>
            <element name="authenticationOnly" type="boolean"
                     minOccurs="0">
                <annotation>
                    <documentation>If present and true, indicates
                        that certificates issued by this CA can only
                        be used for TLS authentication and not for
                        creating and verifying digital
                        signatures/seals.
                    </documentation>
                </annotation>
            </element>
            <element name="topCA" type="tns:CaInfoType">
                <annotation>
                    <documentation>Topmost (usually self-signed) CA
                        that is used as trust anchor.
                    </documentation>
                </annotation>
            </element>
            <element name="intermediateCA" type="tns:CaInfoType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Intermediate CA. This information
                        can be used for certificate path building and
                        finding OCSP responders.
                    </documentation>
                </annotation>
            </element>
            <element name="certificateProfileInfo" type="string">
                <annotation>
                    <documentation>
                        Fully qualified class name implementing the ee.ria.xroad.common.certificateprofile.CertificateProfileInfoProvider interface.
                    </documentation>
                </annotation>
            </element>
            <element name="acmeServer" type="tns:AcmeServer" minOccurs="0">
                <annotation>
                    <documentation>ACME specific certification services settings.</documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="GlobalGroupType">
        <sequence>
            <element name="groupCode" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies the
                        group within an X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="description" type="string">
                <annotation>
                    <documentation>Description of the group.
                    </documentation>
                </annotation>
            </element>
            <element name="groupMember"
                     type="id:XRoadClientIdentifierType" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>Identifier of an X-Road member or
                        a subsystem belonging to this group.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="OcspInfoType">
        <annotation>
            <documentation>Information about an OCSP provider.
            </documentation>
        </annotation>
        <sequence>
            <element name="url" type="string">
                <annotation>
                    <documentation>URL of the OSCP server.
                    </documentation>
                </annotation>
            </element>
            <element name="cert" type="base64Binary" minOccurs="0">
                <annotation>
                    <documentation>Certificate used by the OCSP
                        server to sign OCSP responses.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="ApprovedTSAType">
        <sequence>
            <element name="name" type="string">
                <annotation>
                    <documentation>Name of the time-stamping
                        authority, used in user interfaces.
                    </documentation>
                </annotation>
            </element>
            <element name="url" type="string">
                <annotation>
                    <documentation>URL of the time-stamping service.
                    </documentation>
                </annotation>
            </element>
            <element name="cert" type="base64Binary">
                <annotation>
                    <documentation>Certificate used by the
                        time-stamping server to sign responses.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="CaInfoType">
        <annotation>
            <documentation>This type encapsulates information about a
                certification authority.
            </documentation>
        </annotation>
        <sequence>
            <element name="cert" type="base64Binary">
                <annotation>
                    <documentation>The CA certificate value.
                    </documentation>
                </annotation>
            </element>
            <element name="ocsp" type="tns:OcspInfoType" minOccurs="0"
                     maxOccurs="unbounded">
                <annotation>
                    <documentation>List of OCSP responders that
                        provide status of certificates issued by this
                        CA.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="AcmeServer">
        <sequence>
            <element name="directoryURL" type="string">
                <annotation>
                    <documentation>ACME directory URL that is used as an entrypoint to communicate with the ACME server. The response of this
                        endpoint will return all the other necessary API endpoints for making ACME operations.
                        This is used by the Security Server's code internally to order and receive certificates from the CA
                        automatically.
                    </documentation>
                </annotation>
            </element>
            <element name="ipAddress" type="string" minOccurs="0">
                <annotation>
                    <documentation>ACME server IP address or multiple addresses separated by comma, that Security Server admins can
                        use to whitelist the ACME Server in their firewall rules, so that the ACME server's HTTP challenge
                        wouldn't be blocked.
                    </documentation>
                </annotation>
            </element>
            <element name="authenticationCertificateProfileId" type="string" minOccurs="0">
                <annotation>
                    <documentation>
                        Profile ID used for some ACME servers to let them know the certificate usage type when ordering
                        an authentication certificate.
                    </documentation>
                </annotation>
            </element>
            <element name="signingCertificateProfileId" type="string" minOccurs="0">
                <annotation>
                    <documentation>
                        Profile ID used for some ACME servers to let them know the certificate usage type when ordering
                        a signing certificate.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="SubsystemType">
        <sequence>
            <element name="subsystemCode" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies this
                        subsystem within the subsystems of its
                        parent-member.
                    </documentation>
                </annotation>
            </element>
        </sequence>
        <attribute name="id" type="ID"/>
    </complexType>

    <complexType name="MemberClassType">
        <sequence>
            <element name="code" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies the
                        member class in this X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="description" type="string">
                <annotation>
                    <documentation>Description of the member class.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="CentralServiceType">
        <sequence>
            <element name="serviceCode" type="string">
                <annotation>
                    <documentation>Code that uniquely identifies a
                        central service in this X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="implementingService"
                     type="id:XRoadServiceIdentifierType" minOccurs="0">
                <annotation>
                    <documentation>Identifier of the service that
                        implements the central service.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>

    <complexType name="GlobalSettingsType">
        <sequence>
            <element name="memberClass" type="tns:MemberClassType"
                     minOccurs="0" maxOccurs="unbounded">
                <annotation>
                    <documentation>Lists the member classes used in
                        this X-Road instance.
                    </documentation>
                </annotation>
            </element>
            <element name="ocspFreshnessSeconds" type="integer">
                <annotation>
                    <documentation>Maximum allowed validity time of
                        OCSP responses. If producedAt field of an OCSP
                        response is older than ocspFreshnessSeconds
                        seconds, it is no longer valid.
                    </documentation>
                </annotation>
            </element>
        </sequence>
    </complexType>
</schema>
```