### 3.1 X-Road Message Protocol

X-Road Message Protocol is used by service client and service provider information systems for communicating with the X-Road security server.

The protocol is a synchronous RPC style protocol that is initiated by the client IS or by the service provider's security server.

X-Road provides a message protocol for SOAP and a message protocol for REST. The X-Road Message Protocols are based on SOAP/REST over HTTP(S) and adds additional header fields for identifying the service client and the invoked service. See \[[PR-MESS](#Ref_PR-MESS)\] and \[[PR-REST](#Ref_PR-REST)\] for technical details.

These protocols (together with the Message Transport Protocol) form the core of the X-Road data exchange. If the involved components are not available, then the data exchange is not possible. X-Road architecture makes possible to improve the availability of the involved components by using redundancy.