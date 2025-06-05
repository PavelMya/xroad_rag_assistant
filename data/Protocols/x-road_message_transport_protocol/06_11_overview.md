### 1.1 Overview

<a id="Messtransport_protocol_overview" class="anchor"></a>
![](img/pr-messtransport-protocol-overview.png)

Figure 1. Protocols used in the X-Road system

As can be seen from [Figure 1](#Messtransport_protocol_overview), three protocols are involved when exchanging messages between a service client and a service provider. These include:
- X-Road message protocol – used for communication between an information system and a security server within an organization
  - There are two types of X-Road message protocols, one for SOAP and one for REST
  - X-Road message protocol (for SOAP) is a profile of the SOAP protocol (<http://www.w3.org/TR/2000/NOTE-SOAP-20000508/>).
  See [PR-MESS](#Ref_PR-MESS) for details.
  - X-Road message protocol for REST is a protocol for consuming and producing REST services.
  See [PR-REST](#Ref_PR-REST) for details.
  - Same message protocol needs to be used in both ends. Using _message protocol for REST_ between service client's information system and
  security server, and _message protocol for SOAP_ between service provider's security server and information system is not supported.

- X-Road message transport protocol – a synchronous secure communication protocol that provides confidentiality and integrity when exchanging messages between two security servers over the public Internet. This protocol is described in the current document.

- OCSP Response Retrieval Protocol – the protocol used in parallel with the X-Road message transport protocol when establishing a secure communications channel between the service client's and the service provider's security servers (see [Section 2.2](#22-downloading-ocsp-responses-from-service-provider) for details).

The communication protocol is divided into two layers ([Figure 2](#Messtransport_protocol_layers)) – the transport layer and the application layer. The transport layer uses HTTP over mutually authenticated TLS; see  [Section 2](#2-transport-layer)  for details on how the TLS session is established. The application layer consists of MIME multipart encoded X-Road transport messages that are exchanged over the transport layer (HTTPS); see [Section 3](#3-application-layer) for the exact format of the message and how it's processed.

The service client's security server encapsulates the request message it receives from the service client into an X-Road transport message and in turn receives an X-Road transport message (message format described in [Section 3.1](#31-x-road-transport-message)) from the service provider's security server before forwarding the encapsulated response back to the service client (process described in detail in [Section 3.2](#32-message-handling-in-service-clients-security-server)).
 
The service provider's security server receives the X-Road transport message from the service client's security server and forwards the encapsulated request message to the service provider. The service provider's security server encapsulates the response from the service provider into an X-Road transport message and sends it to the service client's security server (process described in detail in [Section 3.3](#33-message-handling-in-service-providers-security-server)).

Chapters [2](#2-transport-layer) and [3](#3-application-layer), as well as the annex of this specification contain normative information. All the other sections are informative in nature. All the references are normative.

This specification does not include option for partially implementing the protocol – the conformant implementation must implement the entire specification.

<a id="Messtransport_protocol_layers" class="anchor"></a>
![](img/pr-messtransport-protocol-layers.png)

Figure 2. Layers of the X-Road message transport protocol