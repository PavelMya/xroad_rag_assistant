### 2.1 Retrieving Signed Documents of the Entire Transaction

The service requires the identifier of the corresponding message and the X-Road client identifier to determine which signed documents to return. These can be provided with the following mandatory parameters:

* `queryId` –  the X-Road message transaction identifier, which is a part of the SOAP message header;
* `xRoadInstance` – the X-Road instance of the client identifier;
* `memberClass` – the member class of the client identifier;
* `memberCode` – the member code of the client identifier;
* `subsystemCode` – the subsystem code of the client identifier.

Thus, in order to retrieve the signed document for a message with transaction identifier *abc12345* exchanged by security server *sec1.gov* by client *EE/ENT/CLIENT1/SUB*, the request URL is

    http://sec1.gov/asic?queryId=abc12345&xRoadInstance=EE&memberClass=ENT&memberCode=CLIENT1&subsystemCode=SUB

If a message with the given identifier was indeed exchanged by the security server and by the specified client, the server would respond with a ZIP archive (content-type `application/zip`, filename `queryId.zip`), which contains signed documents for all requests and responses that match the specified parameters.

The signed documents provided by the asic service are named `queryId-request-Z.asice[.gpg]` and `queryId-response-Z.asice.[gpg]` for requests and responses, respectively, where `queryId` is the identifier (URL encoded) of the message and `Z` is a up to 13-character alphanumeric string. The `.gpg` suffix is added if the file is encrypted.