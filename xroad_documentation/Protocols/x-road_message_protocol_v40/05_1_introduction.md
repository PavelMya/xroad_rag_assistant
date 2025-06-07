## 1 Introduction

This specification describes the X-Road message protocol version 4.0. This protocol is used between information systems and security servers in the X-Road system. The protocol is implemented as a profile of the SOAP 1.1 protocol \[[SOAP](#Ref_SOAP)\]. Because this protocol inherits the general model, the transport mechanism, and the error handling mechanism of the base SOAP protocol, these issues are not discussed separately in this specification.

Chapters [2](#2-format-of-messages) and [3](#3-describing-services), as well as [Annex A](#annex-a-xml-schema-for-identifiers), [Annex B](#annex-a-xml-schema-for-identifiers) of this specification contain normative information. All the other chapters are informative in nature. All the references are normative.

This specification does not include option for partially implementing the protocol – the conformant implementation must implement the entire specification.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document (in uppercase, as shown) are to be interpreted as described in \[[RFC2119](#Ref_RFC2119)\].

### 1.1 Terms and Abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].