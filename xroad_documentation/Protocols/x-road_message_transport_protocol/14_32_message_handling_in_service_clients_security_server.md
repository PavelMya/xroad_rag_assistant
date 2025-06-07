### 3.2 Message Handling in Service Client's Security Server

The following describes the actions that the service client's security server must take in order to perform a secure message exchange between a service client and a service provider.

1. Receive a REST request, SOAP message or a SOAP message package (if attachments are present) from the service client (message format described in [PR-MESS](#Ref_PR-MESS)).

2. Parse either the SOAP message or `X-Road-Client` header to determine the target service provider.

3. Establish TLS connection with it's security server (see [Section 2.1](#21-tls-authentication)).

4. Send an X-Road transport message to the service provider's security server (message format described in [Section 3.1](#31-x-road-transport-message)) in the following steps:

    a)	For SOAP and REST messages, add the following HTTP headers to the HTTP headers of the HTTP request:

    * UUID (`x-road-request-id`). The id is shared between request/response pairs so one can easily find corresponding messages from logs if needed.

    * Hash algorithm identifier (`x-hash-algorithm`). The hash algorithm is used by the other party to calculate the hashes of the message parts to be used during message verification.

    * Original content type (`x-original-content-type`) of the request message.
    
    * Version (`x-proxy-version`) of the client X-Road proxy
    
    * (only for SOAP messages) original SOAPAction (`x-original-soapaction`)

    b)	For REST messages, add the following additional HTTP header:

    * Message type discriminator (`x-road-message-type`) with value `REST`

    c) Write an OCSP response part to the transport message (content-type `application/ocsp-response`) for each OCSP response in the authentication certificate chain used for establishing the TLS connection.

    d) For SOAP messages, write the service client's request SOAP message (content-type `text/xml` or `application/xop+xml` in case the original message is a MTOM-encoded SOAP message package) to the transport message. Calculate the hash of the request SOAP message.

    e) If the original request was a SOAP message package, write a nested MIME multipart (content-type `multipart/mixed`) containing all attachments as parts. Copy the MIME headers of each attachment part and calculate the hash of the data. 

    f) For REST messages, write the REST request header part (content-type `application/x-road-rest-request`). This part contains HTTP request line and HTTP headers. Calculate the hash of this part.

    * Some new headers must be added (replaced if one already exists) by the security server, for example `x-road-request-id`

    * Some headers must be removed, for example `User-Agent`

    * All other headers must be copied from original request as-is, for example `X-Powered-By`

    * For details, see \[[PR-REST](#Ref_PR-REST)\] and "Use of HTTP Headers"

    g) For REST messages with a request body, write the part containing the REST request body (content-type `application/x-road-rest-body`). Calculate the hash of the body.

    h) Calculate the signature using the stored message and attachment hashes in accordance with \[[PR-SIGDOC](#Ref_PR-SIGDOC), [BATCH-TS](#Ref_BATCH-TS)\]. Write the signature as the last part of the message (content-type `signature/bdoc-1.0/ts`).

5. Start reading a response from the target service provider's security server (message format described in [Section 3.1](#31-x-road-transport-message).

6. If the content-type of the response is `multipart/mixed` then process the message parts as follows:

    a) The first part must be the encapsulated SOAP response message or REST response message. The message is not forwarded to the service client until it can be verified.

    b) SOAP response is identified by content-type `text/xml` or `application/xop+xml` in case the response is a MTOM-encoded SOAP message package. 

    1. If the content-type of the next part is `multipart/mixed` then this part is the nested attachments multipart. 

    c) REST response is identified by content-type `application/x-road-rest-response`
    
    1. REST response header part has content-type `application/x-road-rest-response`. This part contains the HTTP status line and HTTP headers.

    2. If the content-type of the next part is `application/x-road-rest-body` then this part is the body of the REST response. For responses without a body, this part does not exist.
    
    d) If the content-type of the next part is `application/hash-chain-result` then this message contains a batch signature. The hash chain result is stored for message verification.

    e) If the content-type of the next part is `application/hash-chain` then this message contains a batch signature. The hash chain is stored for message verification. The hash chain result must be present if the hash chain is present.

    f) If the content-type of the last part is `signature/bdoc-1.0/ts` then the part contains the signature of the message. If the content-type of the part is `text/xml` then the part contains a SOAP fault indicating that an error occurred during the processing of the message in the service provider's security server and it must be returned to the service client.

If the content-type of the response is `text/xml` then an error occurred at the service provider's security server and the received SOAP Fault must be returned to the service client. In case of any other content-type, the response is malformed and a corresponding SOAP Fault must be returned to the service client.

7. Verify the response message using the stored message hash, attachment hashes, and signature in accordance with \[[PR-SIGDOC](#Ref_PR-SIGDOC), [BATCH-TS](#Ref_BATCH-TS)\].

8. Send the service provider's REST response, encapsulated response SOAP message, or a SOAP message package in case the response has attachments to the service client.

    a) For REST responses, response HTTP headers are copied from `application/x-road-rest-response`


![](img/pr-messtransport-protocol-message-processing-client.svg)

Figure 5. Message processing on service client's side