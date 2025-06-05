## 1 Introduction

This specification describes an extension of the X-Road protocol for targeting a message to a specific security server.

The original X-Road message protocol version 4.0 \[[PR-MESS](#Ref_PR-MESS)\] has the SOAP header element `service` to define the recipient of a message.
In a clustered security server configuration, one service can be served from multiple security servers. When X-Road routes the message to such a service,
it picks the target security server based on which server establishes a connection the quickest.
There is no guarantee about the actual target server &mdash; it can be any of the clustered servers. There are use cases,
like environmental monitoring \[[ARC-ENVMON](#Ref_ARC-ENVMON)\], where targeting messages to a specific security server is needed.
Using the `securityServer` element makes this possible.