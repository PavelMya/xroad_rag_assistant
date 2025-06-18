#### Example 3 (Category 3)

The consumer information system sends a request that doesn't conform to the X-Road Message Protocol for REST. The status
code, response body and HTTP headers are returned by the Security Server.

HTTP status code:

```
400
```

Response body:

```json
{
  "type": "Client.BadRequest",
  "message": "Error parsing the client's REST request. Please that the request format corresponds to the X-Road Message Protocol for REST (r1).",
  "detail": "018cbcae-537e-421b-b6f6-2608dc97bd90"
}
```

HTTP headers:

```http
Date: Thu, 21 Mar 2019 11:45:12 GMT
Content-Type: application/json;charset=utf-8
X-Road-Error: Client.BadRequest
Content-Length: 167
```