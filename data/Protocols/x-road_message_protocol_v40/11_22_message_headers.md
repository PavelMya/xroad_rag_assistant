### 2.2 Message Headers

This section describes additional SOAP headers that are used by the X-Road system. It makes use of data types specified in [Section 2.1](#21-identifiers). The header fields are described in [Table 1](#Ref_Supported_header_fields).


<a name="Ref_Supported_header_fields" class="anchor"></a>
Table 1. Supported header fields

 Field           | Type                                      | Mandatory /Optional | Description
---------------- | ----------------------------------------- | ----------- | --------------------------------------------------------
 client          | XRoadClientIdentifierType                 | M           | Identifies a service client – an entity that initiates the service call.
 service         | XRoadServiceIdentifierType                | O           | Identifies the service that is invoked by the request.
 id              | string                                    | M           | Unique identifier for this message. The recommended form of message ID is UUID.
 userId          | string                                    | O           | User whose action initiated the request. The user ID should be prefixed with two-letter ISO country code (e.g., EE12345678901).
 issue           | string                                    | O           | Identifies received application, issue or document that was the cause of the service request. This field may be used by the client information system to connect service requests (and responses) to working procedures.
 protocolVersion | string                                    | M           | X-Road message protocol version. The value of this field MUST be 4.0
 requestHash     | string                                    | O           | For responses, this field contains a Base64 encoded hash of the request SOAP message. This field is automatically filled in by the service provider's security server.
 requestHash /@algorithmId | string                          | M           | Identifies the hash algorithm that was used to calculate the value of the requestHash field. The algorithms are specified as URIs listed in the XML-DSIG specification \[[DSIG](#Ref_DSIG)\].

When a service client sends a request to the security server, the field `service` MUST be present.

When responding, the service MUST copy all the header fields from the request to the response in the exact same sequence with the exact same values. The XML namespace prefix of the header fields has no significance to the security server, but the prefix must reference the same namespace as in the request.

The `requestHash` field is used to create a strong connection between a request and a response. Thus, it is possible to prove, for example, that a certain registry record is returned in response to a certain query. The `requestHash` is computed from the byte contents of the SOAP request message using the algorithm from the `requestHash/@algorithmId` field. The byte contents of the SOAP request message are:

- in case the request has no attachments – the byte contents of the HTTP POST request sent to the service client's security server;

- in case the request is a multipart MIME message with attachments – the byte contents of the first part of the multipart message. Messages with attachments are described in more detail in [Section 2.4](#24-attachments).

The `requestHash` field MUST be automatically created by the service provider's security server when receiving the service response message and MUST be verified by the service client's security server.

The request message SHOULD NOT contain the `requestHash` field. The response message sent by service to the service provider's security server SHOULD NOT contain the `requestHash` field. If the response message contains the requestHash field, the service provider's security server MUST ignore the field and replace it with the created field.

The `requestHash` field SHOULD NOT be described in the service WSDL.

Content-type and SOAPAction HTTP headers of the client request message are preserved in the security servers and forwarded to the service. All other HTTP headers of the client request message are not preserved by the security servers and are not forwarded to the service.

Content-type HTTP header of the service response message is preserved in the security servers and is forwarded to the client. All other HTTP headers of the service response are not preserved by security servers and are not forwarded to the client.

Starting with X-Road message protocol version 4.0 any protocols with the same major version number are compatible. Minor versions are used to describe backwards compatible changes, such as addition of optional headers.