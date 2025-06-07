### 6.3 PUT Request and Response

REQUEST

| Service       | Method | Description            | Parameters                                          |
|:--------------|:-------|:-----------------------|:----------------------------------------------------|
| /pets/{petId} | PUT    | Update an existing pet | body - Pet object that will be updated in the store |

Service called directly

```bash
curl -X PUT "https://petstore.niis.org/v2/pets/5657082955040009" -H "accept: application/json" -H "Content-Type: application/json" -d '{ "id": 0, "category": { "id": 0, "name": "string" }, "name": "doggie", "photoUrls": [ "string" ], "tags": [ { "id": 0, "name": "string" } ], "status": "available"}'
```

Service called through X-Road

```bash
curl -X PUT "https://{securityserver}/r1/{serviceId}/v2/pets/5657082955040009" -H "accept: application/json" -H "Content-Type: application/json"  -H "X-Road-Client: {client}" -d '{ "id": 0, "category": { "id": 0, "name": "string" }, "name": "doggie", "photoUrls": [ "string" ], "tags": [ { "id": 0, "name": "string" } ], "status": "available"}'
```

Service response

```json
{
  "id": 5657082955040009,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
```

Service response code

```
200
```

Service response headers

```
Date: Thu, 21 Mar 2019 12:43:33 GMT
x-road-id: acdb2c7a-c705-41c2-b595-4cd62e78316e
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: MOEfTqBjdqYiX3db9hxJ6JvHvCpYqfA6t0Uhdv6g2I29fMY8ld4CbN8tslj6mUQPXoRaUdPm7NdZeAYTg6zi+A==
Content-Length: 0
```