### 4.3 Use of HTTP Headers

There is only one mandatory HTTP header in the protocol that needs to be set by the client. Otherwise the use of headers
in X-Road REST service calls is OPTIONAL. The mandatory header and the most common optional header types and their
operation are described next.

Note. HTTP headers are not case-sensitive. `X-Road-Client` and `x-road-client` are both valid header names.

**Mandatory X-Road headers in the request**

- **X-Road-Client**: Specifies the member/subsystem that is used as a service client - an entity that initiates the
  service call. The identifier consists of the following
  parts: `[X-Road instance]/[member class]/[member code]/[subsystem code]`. Including the subsystem code is OPTIONAL.
  The identifier parts MUST be represented as UTF-8 and encoded using \[[PERCENT-ENCODING](#Ref_PERCENTENC)\].
    - The service client MUST NOT generate multiple `X-Road-Client` headers in the request. If multiple `X-Road-Client`
      headers are present in the request, the Security Server SHOULD use the last defined header as the initiator of the
      service call.
  ```http
  X-Road-Client: INSTANCE/CLASS/MEMBER/SUBSYSTEM
  ```

**X-Road specific headers returned in the response**

The response contains some X-Road specific headers that are set by the provider Security Server. The provider service
SHOULD NOT set these headers since in that case they will be overwritten.

- **X-Road-Client**:  Specifies the member/subsystem that is used as a service client
- **X-Road-Service**:  Specifies the serviceId that is invoked by the service client
- **X-Road-Id**: Unique identifier for this message
- **X-Road-Request-Hash**: For responses, this field contains sha-512 encoded hash of the request message
- **X-Road-Error**: This header is provided in case there was an error processing the request and it occurred somewhere
  in X-Road (on the consumer or provider Security Server)
- **X-Road-Request-Id**: Unique identifier for the request
  ```http
  X-Road-Client: INSTANCE/CLASS/MEMBER/SUBSYSTEM
  X-Road-Service: INSTANCE/CLASS/MEMBER/SUBSYSTEM/PETSTORE
  X-Road-Id: fa2e18a5-c2cb-4d09-b994-f57727f7c3fb
  X-Road-Request-Hash: 4c519cf0-0e5e-4ccf-b72b-8ed6fe289e6e
  X-Road-Request-Id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
  ```

**Request hash header**

- **X-Road-Request-Hash**: For responses, this field SHALL contain the base-64 encoded SHA512(SHA512(headers)+SHA512(
  body)). If there is no body, then only the headers are included in the calculation i.e. the field contains the base-64
  encoded SHA512(headers). This field is automatically filled in by the service provider's Security Server. The field is
  used to create a strong connection between a request and a response. Thus, it is possible to prove, for example, that
  a certain registry record is returned in response to a certain query.
- The request hash header MUST be automatically created by the service provider's Security Server
  and it MUST be verified by the service client's Security Server
- The request message SHOULD NOT contain the request hash header.
- The response message returned by a service provider SHOULD NOT contain the request hash header. If the response
  message contains the request hash header, the service provider's Security Server MUST ignore the field and replace it
  with the created field.
  ```http
  X-Road-Request-Hash: 14sEri8SmLNy/DJyTob0ZddAskmdRy5ZUyhbr33iLkaA+gLpWcivUH16fzbuIs7hhs2AnA4lJDloyIihXMlVQA== 
  ```

**Content-Type header**

- With REST messages that include the request body it is RECOMMENDED that the content's media type is indicated with
  this header. Additionally it is RECOMMENDED to use the charset parameter to indicate the character encoding used the
  REST message.
- The REST messages originating from the Security Server (e.g. error messages) MUST include the header and indicate the
  content's type and character encoding with it.
- If Content-Type header is included in the request message by the consumer information system, it MUST be transported
  unmodified through X-Road to the provider information system
- If Content-Type header is included in the response message by the provider information system, it MUST be transported
  unmodified through X-Road to the consumer information system
  ```http
  Content-Type: application/json; charset=utf-8
  Content-Type: multipart/form-data; boundary=something
  ```

In case the service consumer does not provide the `Content-Type` header (or some of its components), the request message
is anyhow passed to the provider service which can decide what to do with it.

**Accept header**

- It is RECOMMENDED that the service consumer advertises the content types it is able to understand by including
  the `Accept` header in the request message.
- If `Accept` header is included in the request message, it MUST be transported unmodified through X-Road to the service
  provider.
  ```http
  Accept: application/xml
  ```

In case the service consumer does not provide the Accept header, the Security Server MUST use the default
content-type `application/json`.

**Security Server, Represented Party and X-Road extension headers**

- **X-Road-Security-Server**: To send the request to a specific Security Server this header needs to be included. It
  contains the following parts:
    - `[X-Road instance]/[member class]/[member code]/[server code]`
- **X-Road-Represented-Party**: The purpose of this header is to allow sending of additional information to the X-Road
  service providers in case when service client represents third party while issuing a query. The query is initiated by
  a third party and the results are also forwarded to that third party, but the request itself is signed by a client
  identified by the `X-Road-Client` header. It contains the following parts:
    - `[member class]/[member code]`
    - Including the member class is OPTIONAL. If the member class is omitted, also the separator `/` must be omitted:
        - `[member code]`
- Other X-Road extension headers are not defined in this document. Rather they are just contracts between information
  systems and X-Road handles them like any user defined header.
  ```http
  X-Road-Security-Server: INSTANCE/MEMBERCLASS/MEMBERCODE/SERVERCODE
  X-Road-Represented-Party: MEMBERCLASS/MEMBERCODE
  ```

**Optional X-Road headers**

- **X-Road-Id**: Unique identifier for this message. It is RECOMMENDED to use universally unique identifiers
  \[[UUID](#Ref_UUID)\]. If `X-Road-Id` is not provided, it SHALL be generated by the consumer Security Server. The
  provider Security Server SHALL include the `X-Road-Id` header in the response message.
- **X-Road-UserId**: User whose action initiated the request. The user ID should be prefixed with two-letter ISO country
  code (e.g., EE12345678901).
- **X-Road-Issue**: Identifies received application, issue or document that was the cause of the service request. This
  field may be used by the client information system to connect service requests (and responses) to working procedures.
  ```http
  X-Road-Id: fa2e18a5-c2cb-4d09-b994-f57727f7c3fb
  X-Road-UserId: EE12345678901
  X-Road-Issue: MT324223MSD
  ```

**X-Road error header**

- X-Road-Error: This header is provided in case there was an error processing the request and it occurred somewhere in
  X-Road (on the consumer or provider Security Server). With it the client can easily distinguish between the errors
  occurring on provider services and errors on X-Road Security Servers. Note that the header does not contain detailed
  error information but is more like a flag indicator to the interested parties. The header contains only the error type
  and the more detailed information such as the HTTP response code, error message body etc. need to be read from the
  response body.
  ```
  Server.ServerProxy.DatabaseError
  ```

**User defined headers**

- User defined HTTP headers (i.e. the headers not mentioned in \[[LIST-OF-HTTP-HEADERS](#Ref_HTTPHEADERS)\] or this
  document) MUST be passed to recipient unmodified by X-Road Security Server.
  ```http
  X-Powered-By: PHP/5.2.17
  X-Pingback: https://example.com/xmlrpc.php
  ```

**Cache headers**

- X-Road does not cache messages. Cache headers MUST be passed as-is and the consumer/provider MAY take advantage of
  this information.
  ```http
  Cache-Control: no-cache, no-store, must-revalidate
  Pragma: no-cache
  ```

**Cross-origin resource sharing**

- Security Server is not designed to be a direct proxy for a web front-end. It does not do anything specific to enable
  cross-origin resource sharing (CORS).

**Filtered headers**

Some HTTP headers MUST be rewritten by the Security Server. The original value, if any, will not be passed through. The
Security Server will either provide a new value or not send the header at all.

- Hop-by-hop headers
    - Connection, Keep-Alive, Proxy-Authenticate, Proxy-Authorization, TE, Trailer, Transfer-Encoding, Upgrade
- Headers that can leak the name or address of the origin host
    - Host
    - User-Agent
    - Server

**Specially handled headers**

Some HTTP headers are handled by the Security Server and the user should not expect that they are passed through X-Road
unmodified.

- Expect
    - Expectation `100 Continue`  MAY be handled locally at the consumer Security Server. Support for other expectations
      is OPTIONAL.
    - (`100 Continue` is the only expectation defined by \[[RFC7231](#Ref_RFC7231)\])
- Content-Length
    - The Security Server MAY change the transfer encoding, thus removing or adding a content-length header as
      necessary.