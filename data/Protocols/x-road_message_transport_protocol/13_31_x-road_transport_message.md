### 3.1 X-Road Transport Message

<a id="Messtransport_message" class="anchor"></a>
![](img/pr-messtransport-message.svg)

Figure 4. X-Road transport messages

The X-Road transport messages are encoded as MIME multipart messages with content-type `multipart/mixed`.

For SOAP messages, the content-type of the client request message is sent from the service client's security server
to the service provider's security server and vice versa using the `x-original-content-type` HTTP header.
The value of the original content type is used to forward the request or response message to the service provider's
or service client's information system. All other HTTP headers sent by the service client's security server or service
provider's security server are not preserved in the security server. MIME headers in the multipart message are preserved.

For REST messages, the content-type of the client request message is sent from the service client's security server
to the service provider's security server and vice versa using the `application/x-road-rest-request` and
`application/x-road-rest-response` parts, which contain "REST header part" of the REST request or response.
REST header part consists of HTTP request line (for requests), HTTP status line (for responses), and HTTP headers (for both).
Besides `Content-Type` header, also other headers may be preserved by the security server, but the processing varies.
Some new headers are added (replaced if one already exists) by the security server, for example `x-road-request-id`.
Some headers will be removed, for example `User-Agent`.
All other headers are passed through as-is, for example `X-Powered-By`.
For details, see \[[PR-REST](#Ref_PR-REST)\] and "Use of HTTP Headers".

The X-Road transport message encapsulates either the SOAP/REST message package that arrives to the security server or a
SOAP fault message (uses content-type `text/xml` instead of `multipart/mixed`). The latter is only sent from the
service provider's security server to the service client's security server if an error occurred before processing the
request message in the service provider's security server. The normal X-Road request message must consist of the
following MIME message parts (see [Figure 4](#Messtransport_message)). The parts are mandatory unless stated otherwise:

1. byte contents of OCSP responses (content-type `application/ocsp-response`) of the service client's security server authentication certificate chain that was used to authenticate the TLS connection;

2. (optional, either this or REST message must exist) the SOAP message (content-type `text/xml` or `application/xop+xml` in case the original message is a MTOM-encoded SOAP message package);

3. (optional) a nested MIME multipart (content-type `multipart/mixed`) containing all attachments as parts. This part is only present if the original SOAP message package contains attachments;

4. (optional, either this or SOAP message must exist) the REST message header (content-type `application/x-road-rest-request`)

5. (optional) a REST request body (content-type `application/x-road-rest-body`) This part is only present if the REST request contains a body.

6. (optional) if the signature is a batch signature, then:

    a) the hash chain result XML (content-type `application/hash-chain-result`) and

    b)	the hash chain XML (content-type `application/hash-chain`) of the signature.

7. the signature XML (content-type `signature/bdoc-1.0/ts`) associated with the SOAP/REST message and any attachments of the encapsulated message;

The normal X-Road response message must consist of the following MIME message parts (see [Figure 4](#Messtransport_message)). The parts are mandatory unless stated otherwise:

1. (optional, either this or REST message must exist) the SOAP message (content-type `text/xml` or `application/xop+xml` in case the original message is a MTOM-encoded SOAP message package);

2. (optional) a nested MIME multipart (content-type `multipart/mixed) containing all attachments as parts. This part is only present if the original SOAP message package contains attachments;

3. (optional, either this or SOAP message must exist) the REST message header (content-type `application/x-road-rest-response`)

4. (optional) a REST response body (content-type `application/x-road-rest-body`) This part is only present if the REST response contains a body.

5. (optional) if the signature is a batch signature, then:

    a)	the hash chain result XML (content-type `application/hash-chain-result`) and

    b)	the hash chain XML (content-type `application/hash-chain`) of the signature.

6. one of the following:

    a)	the signature XML (content-type `signature/bdoc-1.0/ts`) associated with the SOAP message and any attachments of the encapsulated message; or

    b)	a SOAP fault XML (content-type `text/xml`), if any errors occurred during the processing of the message (i.e. error when creating signature). Since the previous parts of the message have already been sent to the other party, the SOAP fault must be sent as the last part.