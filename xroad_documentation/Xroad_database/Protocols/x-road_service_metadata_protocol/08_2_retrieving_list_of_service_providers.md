## 2 Retrieving List of Service Providers

Security server clients can retrieve a list of all the potential service providers (i.e., members and subsystems) of an X-Road instance. This can be accomplished by making a HTTP GET request to the security server. The request URL is `http://SECURITYSERVER/listClients` or `https://SECURITYSERVER/listClients` depending on whether the HTTPS protocol is configured for interaction between the security server and the information system. When making the request, the address `SECURITYSERVER` must be replaced with the actual address of the security server.
In addition, it is possible to retrieve a list of clients in other, federated X-Road instances by adding the following HTTP parameter:

* `xRoadInstance` – code that identifies the X-Road instance.

Thus, in order to retrieve a list of clients defined in the X-Road instance `AA`, the request URL is `http://SECURITYSERVER/listClients?xRoadInstance=AA`.

It is possible to control the response content type using HTTP `Accept` header. If the header value is `application/json`, the security server must produce an application/json response, as defined in Annex B, [OpenAPI definition](#openapi-definition). Otherwise, security server MUST respond with content-type `text/xml` and the response MUST contain the `clientList` XML element defined in Annex [A](#annex-a-xml-schema-for-messages)).

Annex [C.1](#c1-listclients-response) contains an example XML and JSON response messages

The X-Road client identifier has a hierarchical structure consisting of X-Road instance, member class, member and (optionally) subsystem codes. See specification \[[PR-MESS](#Ref_PR-MESS)\] for explanation and specification of identifiers.