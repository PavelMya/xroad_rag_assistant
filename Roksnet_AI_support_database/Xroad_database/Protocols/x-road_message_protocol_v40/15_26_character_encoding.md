### 2.6 Character Encoding

All parties SHOULD indicate the character encoding of XML messages. The preferred way of specifying the character encoding is by using the *charset* parameter the of *Content-Type* header.

In case the *charset* parameter is not determined in the HTTP *Content-Type* header, the UTF-8 encoding is considered to use by the security server.

With UTF-8 encoding BOM (Byte Order Mark) bytes MAY be used in the beginning of XML message. Security servers MAY remove the BOM bytes when processing the message.