#### 3.7.1 Note on logged X-Road message headers

If the messagelog add-on has the message body logging disabled, only a preconfigured set of the SOAP headers and/or
REST HTTP headers will be included in the message log.

**SOAP**

The logged SOAP headers are the X-Road message headers listed in [Chapter 2.2](../Protocols/pr-mess_x-road_message_protocol.md#22-message-headers) of
the X-Road Message Protocol document \[[PR-MESS](#Ref_PR-MESS)\], as well as the `representedParty` extension of the X-Road protocol described in the
extension's [XML schema](http://x-road.eu/xsd/representation.xsd). The security server targeting extension for the X-Road message protocol
\[[PR-TARGETSS](#Ref_PR-TARGETSS)\] or the Security Token Extension \[[PR-SECTOKEN](#Ref_PR-SECTOKEN)\] will not be included in the message log.

**REST**

The logged HTTP headers are the X-Road HTTP headers listed in [Chapter 4.3](../Protocols/pr-rest_x-road_message_protocol_for_rest.md#43-use-of-http-headers) of
the X-Road Message Protocol for REST document \[[PR-REST](#Ref_PR-REST)\], including the security server targeting
extension for the X-Road message protocol \[[PR-TARGETSS](#Ref_PR-TARGETSS)\]. All other HTTP headers are excluded from
the message log.