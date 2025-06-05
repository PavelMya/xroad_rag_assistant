## 1 Introduction

Management services are services provided by the X-Road governing organization to manage Security Servers and Security Server clients. They are called by Security Servers to register in Central Server the configuration changes made by the Security Server administrator. The management services are the following:

* *clientReg* – registering an X-Road subsystem as a client of the Security Server;

* *clientDeletion* – removing a client from the Security Server;

* *authCertReg* – adding an authentication certificate to the Security Server;

* *authCertDeletion* – removing an authentication certificate from the Security Server.
  
* *ownerChange* - changing the owner member of the Security Server.
  
* *addressChange* - changing Security Server's address.

* *clientDisable* - disabling Security Server's client subsystem temporarily.

* *clientEnable* - enabling disabled Security Server's client subsystem.


The management services are implemented as standard X-Road services (see \[[PR-MESS](#Ref_PR-MESS)\] for detailed description of the protocol) that are offered by the X-Road governing authority. The exception is the *authCertReg* service that, for technical reasons, is implemented as HTTPS POST (see below for details).

This protocol builds on existing transport and message encoding mechanisms. Therefore, this specification does not cover the technical details and error conditions related to making HTTPS requests together with processing MIME-encoded messages. These concerns are discussed in detail in their respective standards.

Section 2 as well as [Annex B](#annex-b-wsdl-file-for-management-services), of this specification contain normative information. All the other sections are informative in nature. All the references are normative.

This specification does not include option for partially implementing the protocol – the conformant implementation must implement the entire specification.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document (in uppercase, as shown) are to be interpreted as described in \[[REQUIREMENT](#Ref_REQ)\].