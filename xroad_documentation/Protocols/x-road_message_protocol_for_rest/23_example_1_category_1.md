#### Example 1 (Category 1)

Everything worked in the Security Server's perspective, but the service returned an error. Status code, response body
and HTTP headers are generated by the provider information system and they are returned as-is.

HTTP status code:

```
405
```

Response body:

```json
{
  "timestamp": "2019-03-21T09:45:19.904Z",
  "status": 405,
  "error": "Method Not Allowed",
  "message": "Request method 'PUT' not supported",
  "path": "/v3/pet/findByStatus"
}
```

HTTP headers:

```http
Content-Type: application/json;charset=utf-8
Date: Thu, 21 Mar 2019 09:45:19 GMT
x-road-id: 5ea48ae9-15c1-465a-be15-9b6ef2c7ef4a
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: yFOLGuJ0zmLhZSgwp3ooSBQbR9ejSvTc6p6FvBmcSEB2tDD6bxpjiv8sHORxqz4MMgEADH7IcARNprLfEwudNw==
Content-Length: 159
```