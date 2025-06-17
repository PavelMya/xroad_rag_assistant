### 4.1 REST Interface

HTTP version 1.1 is used by the protocol as described in \[[RFC2616](#Ref_RFC2616)\]. The consumer member/subsystem is
specified using HTTP headers. The service to be called is encoded as part of the HTTP/HTTPS request URL. Here is the
generic form of the REST service call.

**Request format**

```http
{http-request-method} /{protocol-version}/{serviceId}[/path][?query-parameters]
```

**HTTP request headers**

```http
X-Road-Client: {client}
```

- **{http-request-method}** can be one of the request methods defined in \[[RFC7231](#Ref_RFC7231)\]. For example `GET`
  , `POST`, `PUT` and `DELETE`.
- **{protocol-version}**: specifies the major version of the X-Road Message Protocol for REST. For the initial
  version `r1` MUST be used.
- **{client}**: specifies the member/subsystem that is used as a service client - an entity that initiates the service
  call. The identifier consists of the following
  parts: `[X-Road instance]/[member class]/[member code]/[subsystem code]`. Including the subsystem code is OPTIONAL.
- **{serviceId}** identifies the service that is registered under {provider-subsystem} and invoked by the request.
  {serviceId} contains the following parts:
    - `[X-Road instance]/[member class]/[member code]/[subsystem code]/[service code]`. Including the subsystem code is
      OPTIONAL.
    - The **{serviceId}** is mapped to an actual service URL by the Security Server (see the example below).
- **\[path\]** contains the relative path to the service to be called
- **\[query-parameters\]** contains the query parameters to be sent to the service

Here is a practical example of an X-Road REST call.

**Request example**

```http
GET /r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/BARSERVICE/v1/bar/zyggy?quu=1
```

**HTTP request headers**

```http
X-Road-Client: INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1
```

Breakdown of the request URI:

- **{http-request-method}**: `GET`
- **{protocol-version}**: `/r1`
- **{client}**: `INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1`
- **{serviceId}**: `/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/BARSERVICE`
- **\[path\]**: `/v1/bar/zyggy`
- **\[query-parameters\]**: `?quu=1`

Assuming that the serviceId maps to the URL https://barservice.example.org/, the provider will see the
request `GET https://barservice.example.org/v1/bar/zyggy?quu=1`. The reason for naming the service independently of the
path is that the same provider could have a fooservice as well (https://fooservice.example.org/), in which case it would
be difficult to tell the services apart if the path was the service Id (both services could have paths like "/v1/...")
unless the fooservice was attached to a separate subsystem.