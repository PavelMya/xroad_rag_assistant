## 2 Format of messages

This section describes the XML format for expressing the target security server. The data
structures and elements defined in this section are in the namespace `http://x-road.eu/xsd/xroad.xsd`. This is the same
namespace as defined by the X-Road Message Protocol 4.0 \[[PR-MESS](#Ref_PR-MESS)\] Annex B, XML Schema for Messages. The
schema file can be found at [`http://x-road.eu/xsd/xroad-securityserver.xsd`](http://x-road.eu/xsd/xroad-securityserver.xsd).

Note that at the moment, there is no unifying schema that would combine the message protocol and this extension under
the same namespace. That means there is no single schema that would validate an X-Road message with this extension in use.
It should be possible to validate the messages using a validator that accepts multiple schemas from the same namespace.

In addition, this extension is a candidate for inclusion in the next version of the X-Road message protocol and would then
be part of the actual [`http://x-road.eu/xsd/xroad.xsd`](http://x-road.eu/xsd/xroad.xsd) schema as well as the namespace.

The XML Schema for this extension is listed in the section [XML Schema for the extension](#xml-schema-for-the-extension).