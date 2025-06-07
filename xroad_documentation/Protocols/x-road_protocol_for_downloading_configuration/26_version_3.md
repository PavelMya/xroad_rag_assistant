### Version 3

- Changes in version 3:
    - *source* element of type *ConfigurationSourceType* was added into *SharedParametersType* as the basis to "automatic configuration signing keys' rotation" feature.
    - *acmeServer* complex element was added into *ApprovedCaType* to introduce support for ACME specific certification services.
    - *any* element was added into *SharedParametersType* to enable the ability to add new optional elements without breaking backwards compatibility (i.e. without breaking the schema validation on older Security Servers).

```xml


    

    
        
            Set of configuration parameters that are
                used by members of this X-Road instance and other
                federated instances.
            
        
    

    
        
            
                
                    Code that uniquely identifies this
                        instance of the X-Road system within a
                        federation of systems.
                    
                
            
            
                
                    Describes one configuration source.
                    
                
            
            
                
                    Certification authority approved
                        by the Governing Authority of providing
                        certification services for members of this
                        X-Road instance.
                    
                
            
            
                
                    Time-stamping authority approved
                        by the Governing Authority of providing
                        time-stamping services for members of this
                        X-Road instance.
                    
                
            
            
                
                    Registered member of this X-Road
                        system.
                    
                
            
            
                
                    Security server registered in this
                        X-Road system.
                    
                
            
            
                
                    Group of access rights subjects,
                        defined by the Governing Authority. An access
                        rights subject can be either a member or a
                        subsystem.
                    
                
            
            
                
                    Central service, defined by the
                        Governing Authority.
                    
                
            
            
                
                    Classifiers and security policy
                        settings used in this X-Road instance.
                    
                
            
            
        
    

    
        
            
                
                    The address of the central server which provides the signed configuration.
                
            
            
                
                    Public key that can be used to verify the signed configuration, presented as X.509 certificate.
                
            
            
                
                    Public key that can be used to verify the signed configuration, presented as X.509 certificate.
                
            
        
    

    
        
            
                
                    Member class of the member.
                    
                
            
            
                
                    Code that uniquely identifies the
                        member within the given member class.
                    
                
            
            
                
                    Full, official name of the member,
                        used in user interfaces.
                    
                
            
            
                
                    Represents information about a
                        part of the member's information system that
                        is acting as an independent service consumer
                        or provider in the X-Road system.
                    
                
            
        
        
    

    
        
            
                
                    Identifier of the member who is
                        responsible for the security server.
                    
                
            
            
                
                    Code that uniquely identifies this
                        server within servers owned by the same
                        member.
                    
                
            
            
                
                    Externally visible address of the
                        security server.
                    
                
            
            
                
                    Hash of the authentication
                        certificate used by the security server.
                    
                
            
            
                
                    Identifier a registered client of
                        this security server. Client can be either a
                        member or a subsystem.
                    
                
            
        
    

    
        
            
                
                    Name of the CA, used in user
                        interfaces.
                    
                
            
            
                
                    If present and true, indicates
                        that certificates issued by this CA can only
                        be used for TLS authentication and not for
                        creating and verifying digital
                        signatures/seals.
                    
                
            
            
                
                    Topmost (usually self-signed) CA
                        that is used as trust anchor.
                    
                
            
            
                
                    Intermediate CA. This information
                        can be used for certificate path building and
                        finding OCSP responders.
                    
                
            
            
                
                    
                        Fully qualified class name implementing the ee.ria.xroad.common.certificateprofile.CertificateProfileInfoProvider interface.
                    
                
            
            
                
                    ACME specific certification services settings.
                
            
        
    

    
        
            
                
                    Code that uniquely identifies the
                        group within an X-Road instance.
                    
                
            
            
                
                    Description of the group.
                    
                
            
            
                
                    Identifier of an X-Road member or
                        a subsystem belonging to this group.
                    
                
            
        
    

    
        
            Information about an OCSP provider.
            
        
        
            
                
                    URL of the OSCP server.
                    
                
            
            
                
                    Certificate used by the OCSP
                        server to sign OCSP responses.
                    
                
            
        
    

    
        
            
                
                    Name of the time-stamping
                        authority, used in user interfaces.
                    
                
            
            
                
                    URL of the time-stamping service.
                    
                
            
            
                
                    Certificate used by the
                        time-stamping server to sign responses.
                    
                
            
        
    

    
        
            This type encapsulates information about a
                certification authority.
            
        
        
            
                
                    The CA certificate value.
                    
                
            
            
                
                    List of OCSP responders that
                        provide status of certificates issued by this
                        CA.
                    
                
            
        
    

    
        
            
                
                    ACME directory URL that is used as an entrypoint to communicate with the ACME server. The response of this
                        endpoint will return all the other necessary API endpoints for making ACME operations.
                        This is used by the Security Server's code internally to order and receive certificates from the CA
                        automatically.
                    
                
            
            
                
                    ACME server IP address or multiple addresses separated by comma, that Security Server admins can
                        use to whitelist the ACME Server in their firewall rules, so that the ACME server's HTTP challenge
                        wouldn't be blocked.
                    
                
            
        
    

    
        
            
                
                    Code that uniquely identifies this
                        subsystem within the subsystems of its
                        parent-member.
                    
                
            
        
        
    

    
        
            
                
                    Code that uniquely identifies the
                        member class in this X-Road instance.
                    
                
            
            
                
                    Description of the member class.
                    
                
            
        
    

    
        
            
                
                    Code that uniquely identifies a
                        central service in this X-Road instance.
                    
                
            
            
                
                    Identifier of the service that
                        implements the central service.
                    
                
            
        
    

    
        
            
                
                    Lists the member classes used in
                        this X-Road instance.
                    
                
            
            
                
                    Maximum allowed validity time of
                        OCSP responses. If producedAt field of an OCSP
                        response is older than ocspFreshnessSeconds
                        seconds, it is no longer valid.
                    
                
            
        
    

```