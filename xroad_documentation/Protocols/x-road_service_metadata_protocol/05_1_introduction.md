## 1 Introduction

This specification describes methods that can be used by X-Road participants to discover what services are available to them and download the WSDL files describing these services. The X-Road service metadata protocol is intended to support portals and other software that can discover the available services and then automatically generate user interfaces based on their descriptions. In order to accomplish this, the portal can use the following steps.

1. Download a list of X-Road members and subsystems (see Section [2](#2-retrieving-list-of-service-providers)). This results in a list of (potential) service provides who can be further be queried.

2. Connect to the service provider and acquire a list of services offered by this provider (see Section [4](#4-retrieving-list-of-services)). This service has two forms: `listMethods` returns a list of services provided by a given service provider, `allowedMethods` constrains the returned list by only including services that are allowed for the client.

3. Download the description of the service in WSDL format (see Section [5](#5-retrieving-the-wsdl-of-a-service)).

This specification is based on the X-Road protocol \[[PR-MESS](#Ref_PR-MESS)\]. The X-Road protocol specification also defines important concepts used in this text (for example X-Road identifier). Because this protocol uses HTTP and X-Road protocol as transport mechanisms, the details of message transport and error conditions are not described in this specification.

Chapters [2](#2-retrieving-list-of-service-providers), [3](#4-retrieving-list-of-services) and [4](#5-retrieving-the-wsdl-of-a-service) together with annexes [A](#annex-a-xml-schema-for-messages) and [B](#annex-b-listmethods-allowedmethods-and-getwsdl-service-descriptions) contain normative information. All the other sections are informative in nature. All the references are normative.

This specification does not include option for partially implementing the protocol – the conformant implementation must implement the entire specification.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document (in uppercase, as shown) are to be interpreted as described in \[[RFC2119](#Ref_RFC2119)\].

### 1.1 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].