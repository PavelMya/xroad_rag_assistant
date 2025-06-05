### 3.3 Message Handling in Service Provider's Security Server

The following describes the actions that the service provider's security server must take in order to perform a secure message exchange between a service client and a service provider.

1. Establish TLS connection with the service client's security server (see [Section 2.1](#21-tls-authentication)).

2. Start reading the X-Road transport message from the service client's security server (message format described in [Section 3.1](#31-x-road-transport-message)).

3. The content-type of the request message must be `multipart/mixed`. The security server must process the message parts as follows:

    a) Read all the parts with content-type `application/ocsp-response`. These parts contain OCSP responses that must be used in when verifying the authentication certificate chain of the service client's security server.

    b) The part that comes after OCSP responses must be either a SOAP or REST request
    
    c) SOAP request is identified by content-type `text/xml` or `application/xop+xml`

    1. If content-type is `text/xml`, this part contains a regular SOAP request. If content-type is `application/xop+xml` this part contains the encapsulated SOAP request message for a MTOM-encoded SOAP message package. The message is not forwarded to the service provider until it can be verified.

    2. If the content-type of the next part is `multipart/mixed` then this part is the nested attachments multipart.

    d) REST request is identified by content-type `application/x-road-rest-request`

    1. REST request header part has content-type `application/x-road-rest-response`. This part contains the HTTP request line and HTTP headers.

    2. If the content-type of the next part is `application/x-road-rest-body` then this part is the body of the REST request. For requests without a body, this part does not exist.

    d) If the content-type of the next part is `application/hash-chain-result` then this message contains a batch signature. The hash chain result is stored for message verification.

    e) If the content-type of the next part is `application/hash-chain` then this message contains a batch signature. The hash chain is stored for message verification.

    f) If the content-type of the last part is `signature/bdoc-1.0/ts` then the part contains the signature of the message. If the content-type of the last part is `text/xml` then the part contains a SOAP fault indicating that an error occurred during the processing of the message in the service client's security server.

4. Verify the request message using the stored message hash, attachment hashes, and signature in accordance with \[[PR-SIGDOC](#Ref_PR-SIGDOC), [BATCH-TS](#Ref_BATCH-TS)\].

5. Either send the encapsulated SOAP message and any attachments to the target service provider, or execute a REST request against target service provider.

6. Start reading a response from the target service provider (message format described in [PR-MESS](#Ref_PR-MESS)).

7. Send an X-Road transport message to the service client's security server (message format described in [Section 3.1](#31-x-road-transport-message)) in the following steps:

    a) Add the following HTTP headers to the HTTP headers of the HTTP request:

    * Hash algorithm identifier (`x-hash-algorithm`). The hash algorithm is used by the other party to calculate the hashes of the message parts to be used during message verification.

    * Only in the case of SOAP messages, original content type (`x-original-content-type`) of the request message.

    b) For SOAP messages, write the service provider's response SOAP message (content-type `text/xml` or `application/xop+xml` in case the original message is a MTOM-encoded SOAP message package). Calculate the hash of the response SOAP message to be used when creating the signature.

    c) If the response from the service provider was a SOAP message package, write a nested MIME multipart (`multipart/mixed`) containing all attachments as parts. For each part, calculate the hash of the data to be used when creating the signature.

    d) For REST messages, write the REST response header part (content-type `application/x-road-rest-response`). This part contains HTTP status line and HTTP headers. Calculate the hash of the response message to be used when creating the signature.

    * Some new headers must be added (replaced if one already exists) by the security server, for example `x-road-request-id`

    * Some headers must be removed, for example `User-Agent`

    * All other headers must be copied from original request as-is, for example `X-Powered-By`

    * For details, see \[[PR-REST](#Ref_PR-REST)\] and "Use of HTTP Headers"

    e) If the response from the service provider contained a REST message body, write the part containing this (content-type `application/x-road-rest-body`). Calculate the hash of the body to be used when creating the signature. 

    f) Calculate the signature using the stored message and attachment hashes in accordance with \[[PR-SIGDOC](#Ref_PR-SIGDOC), [BATCH-TS](#Ref_BATCH-TS)\]. Write the signature as the last part of the message (content-type `signature/bdoc-1.0/ts`).
    
<a id="Messtransport_protocol_message_processing_service_provider" class="anchor"></a>
![](img/pr-messtransport-protocol-message-processing-service-provider.svg)

Figure 6. Message processing on service provider's side