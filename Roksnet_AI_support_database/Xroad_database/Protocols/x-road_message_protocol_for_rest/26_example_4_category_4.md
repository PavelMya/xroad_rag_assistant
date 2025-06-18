#### Example 4 (Category 4)

Error occurred on the provider Security Server. The status code, response body and HTTP headers are returned by the
Security Server.

HTTP status code:

```
500
```

Response body:

```json
{
  "type": "Server.ServerProxy.DatabaseError",
  "message": "Error accessing database (serverconf)",
  "detail": "3c4d0f08-440f-417f-b935-bc801e103d51"
}
```

HTTP headers:

```http
Date: Thu, 21 Mar 2019 11:57:11 GMT
Content-Type: application/json;charset=utf-8
X-Road-Error: Server.ServerProxy.DatabaseError
Content-Length: 141
```