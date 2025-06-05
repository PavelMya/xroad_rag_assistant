## 1 Introduction

This specification describes protocol that is used to distribute configuration to security servers of an X-Road installation. Additionally, the same protocol is used to distribute configuration between two federated X-Road instances.

This protocol is based on HTTP and MIME protocols and supports refreshing the configuration meta-info without having to download the actual configuration files. The configuration parameters are distributed in XML format and described using XML Schema [XMLSCM1], [XMLSCM2].

This protocol builds on existing transport and message encoding mechanisms. Therefore, this specification does not cover the technical details and error conditions related to downloading information over HTTP and decoding MIME messages. These concerns are discussed in detail in their respective standards.

The chapter [2 Protocol for Downloading Configuration](#2-protocol-for-downloading-configuration) as well as appendices [Annex B](#annex-b-shared-parametersxsd), [Annex C](#annex-c-private-parametersxsd) and [Annex E](#annex-e-configuration-anchorxsd) of this specification contain normative information. All the other sections are informative in nature. All the references are normative.

This specification does not include option for partially implementing the protocol – the conformant implementation must implement the entire specification.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document (in uppercase, as shown) are to be interpreted as described in [RFC2119].