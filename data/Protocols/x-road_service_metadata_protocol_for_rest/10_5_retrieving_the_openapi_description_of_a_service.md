## 5 Retrieving the OpenAPI description of a Service

X-Road provides a metaservice for fetching service descriptions of REST services.

* `getOpenAPI` returns the OpenAPI service description of a REST service

The method is invoked as regular X-Road REST service (see specification \[[PR-REST](#Ref_PR-REST)\] for details on the
X-Road REST protocol).

The serviceId MUST contain the identifier of the target service provider and the value of the serviceCode element MUST
be `getOpenAPI`.

The query parameters must contain `serviceCode=xxx` where xxx is the service code of the REST service we want to get the
service description from.

Request example

```http
GET /r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/getOpenAPI?serviceCode=listFirms
```

HTTP request headers

```http
X-Road-Client: INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1
```

Note that fetching the OpenAPI service description respects the "Verify TLS Certificate" setting of the service.

The body of the response MUST contain the OpenAPI service description of the REST service indicated by the query
parameters.

Annex [A](#annex-a-service-descriptions-for-rest-metadata-services) contains the OpenAPI description of the REST
metadata services.

Annex [B.3](#b3-getopenapi-response) contains an example response message for the service.