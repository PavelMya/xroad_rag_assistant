### 3.1 Scope and Requirements

- X-Road SHALL support both SOAP and REST protocols side by side. This document describes only the X-Road Message
  Protocol for REST. The X-Road Message Protocol for SOAP and the X-Road Message Transport Protocol are described in
  other documents.
- Only synchronous request-response messages SHALL be supported. Asynchronous or one-way operations SHALL NOT be
  possible.
- Any payload type over REST SHALL be supported. The payload MUST NOT be restricted to just JSON or XML.
- The protocol SHALL support any message size. In practice the message size is limited by the Security Server's memory
  and disk sizes. For security reasons it is RECOMMENDED to introduce a configurable "maximum message size" parameter in
  the Security Server implementation.
- HTTP/1.1 SHALL be supported.