### 6.8 Global configuration concepts

**Configuration** – Set of parameters that are distributed by a configuration source. Configuration consists of one or more configuration parts that contain groups of related parameters.

**Configuration Anchor** – is a set of information that can be used by configuration clients to access a configuration source and to verify the downloaded configuration. The configuration anchor is distributed as either a separate XML file in case the anchor points to a local configuration source or as a part of private parameters in case the anchor points to the configuration source managed by a federation partner.

**Configuration Client** – is an entity that uses configuration anchor(s) for downloading configuration from configuration source(s). In an X-Roads system, security server and configuration proxy act as configuration clients. 

**Configuration part (file)** – is an XML file containing system parameters.

**Configuration Provider** – is an entity responsible for maintaining and distributing global configuration. The configuration provider manages one or two configuration sources through which configuration is made available for configuration clients. In an X-Roads system, the central server and the configuration proxy act as configuration providers.

**Configuration Source** – is a component (HTTP server) managed by a configuration provider. The configuration distributed by the source can either be internal configuration or external configuration. The information needed to access and download configuration from a source is contained in the configuration anchor.

**External configuration** – is distributed by a configuration source and only contains the shared parameters configuration part.

**Global configuration** – a technical solution, through which X-Road governing authority regulates participants of X-Road. Global configuration consists of XML-files, which are downloaded periodically from the central server of X-Road governing authority by security servers. Global configuration includes following information:

-   the addresses and public keys of trust anchors (certification service CAs and time stamping services);

-   the public keys of intermediate CAs;

-   the addresses and public keys of OCSP services (if not already available through the certificates' *Authority Information Access* extension);

-   information about X-Road members and their subsystems;

-   the addresses of the members' security servers registered in X-Road;

-   information about the security servers' authentication certificates registered in X-Road;

-   information about the security servers' clients registered in X-Road;

-   information about global access rights groups;

-   X-Road system parameters.  

**Internal configuration** – is distributed by a configuration source and is composed of the following configuration parts: private parameters; shared parameters, and; optionally, other configuration parts that are specific to an X-Road instance – optional parameters.

**Monitoring Parameters** – Set of parameters that control monitoring of security servers

**Optional parameters** – is an optional configuration part that carries system parameters that have a contextual meaning only to a specific X-Road system installation.

**Private parameters** – is a configuration part that holds system parameters that are only used by security servers that are part of the local X-Road system (i.e. the same X-Road system as the central server the configuration part originates from). In case of federated X-Road systems, the private parameters contain configuration anchors pointing to configuration sources distributing external configuration of federation partners.

**Shared parameters** – is a configuration part that holds system parameters that are used both by the security servers of the local X-Road system and by the security servers belonging to X-Road systems federated with the local system.

**Trusted anchor** – is a configuration anchor that points to the external configuration source of a federation partner and has been uploaded to the central server during the federation process. Trusted anchors are distributed to the configuration clients of the local X-Road system as a part of private parameters.

## 7 Technical terms

### 7.1 Trust and security terminology

**CA** - Certification Authority    

**HSM** – Hardware security module

**OCSP** – Online Certificate Status Protocol 

**SSH** - Secure Shell

**TLS** - Transport Layer Security

**TSA** - Timestamping Authority 

**TSP** - Time Stamp Provider