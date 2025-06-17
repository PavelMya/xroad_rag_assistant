#### Example 2 (Category 2)

Everything worked in the Security Server's perspective, but the service timed out. The status code, response body and
HTTP headers are returned by the Security Server.

HTTP status code:

```
500
```

Response body:

```json
{
  "type": "Server.ServerProxy.NetworkError",
  "message": "Connect to 10.139.178.1:8080 [/10.139.178.1] failed: Connection timed out (Connection timed out)",
  "detail": "9bc95b6e-2f1d-4a41-a7e6-11eda7d734d5"
}
```

HTTP headers:

```http
Date: Thu, 21 Mar 2019 11:42:03 GMT
Content-Type: application/json;charset=utf-8
X-Road-Error: Server.ServerProxy.NetworkError
Content-Length: 199
```