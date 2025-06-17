## 4 Retrieving List of Services

X-Road provides two methods for getting the list of services and service endpoints offered by an X-Road client:

* `listMethods` lists all REST services and service endpoints offered by a service provider.

* `allowedMethods` lists all REST services and service endpoints offered by a service provider that the caller has
  permission to invoke. Notice that the endpoints may contain wildcards and the amount of concrete endpoints may
  actually be larger. Generally, fetching the OpenAPI service description is the preferred method for discovering
  service endpoints.

Both methods are invoked as regular X-Road REST services (see specification \[[PR-REST](#Ref_PR-REST)\] for details on
the X-Road REST protocol).

The serviceId MUST contain the identifier of the target service provider and the value of the serviceCode element MUST
be either `listMethods` or `allowedMethods`.

Request example

```http
GET /r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/listMethods
```

HTTP request headers

```http
X-Road-Client: INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1
```

The body of the response message MUST contain a list of services and service endpoints provided by the service
provider (in case of listMethods) or open to the given client (in case of allowedMethods). The response SHALL NOT
contain names of the metainfo services.

Annex [A](#annex-a-service-descriptions-for-rest-metadata-services) contains the OpenAPI description of the REST
metadata services.

Annexes [B.1](#c1-listmethods-response) and [B.2](#c2-allowedmethods-response) contain example response messages for
services, respectively.