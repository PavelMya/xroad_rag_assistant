### 1.1 Overview

Representational State Transfer \[[REST](#Ref_RFC2119)\] is an architectural style that
defines a set of constraints to be used for creating web services. Web
services that conform to the \[[REST](#Ref_RFC2119)\] architectural style, or RESTful web
services, provide interoperability between computer systems on the
Internet. REST-compliant web services allow the requesting systems to
access and manipulate representations of web resources by using a
uniform and predefined set of stateless operations. In the REST
architectural style, the client and server implementations can be
independent as long as they know the format of messages to send each
other.

This document describes the X-Road Message Protocol for \[[REST](#Ref_RFC2119)\]. The protocol is used in X-Road
infrastructure between information systems and X-Road Security Servers to consume and produce REST
services. Between the Security Servers there is another protocol called X-Road Message Transport
Protocol which is described in its own document \[[PR-MESSTRANSP](#Ref_XMESSTP)\].

![](img/message-protocol-for-rest.png)