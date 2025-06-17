### 6.4 POST Request and Response

REQUEST

| Service       | Method | Description                | Parameters                                            |
|:--------------|:-------|:---------------------------|:------------------------------------------------------|
| /pets         | POST   | Add a new pet to the store | body - Pet object that needs to be added to the store |

Service called directly

```bash
curl -X POST "https://petstore.niis.org/v2/pets" -H "accept: application/json" -H "Content-Type: application/json" -d '{ "id": 0, "category": { "id": 0, "name": "string" }, "name": "doggie", "photoUrls": [ "string" ], "tags": [ { "id": 0, "name": "string" } ], "status": "available"}'
```

Service called through X-Road

```bash
curl -X POST "https://{securityserver}/r1/{serviceId}/v2/pets" -H "accept: application/json" -H "Content-Type: application/json" -H "X-Road-Client: {client}" -d '{ "id": 0, "category": { "id": 0, "name": "string" }, "name": "doggie", "photoUrls": [ "string" ], "tags": [ { "id": 0, "name": "string" } ], "status": "available"}'
```

Service response

```json
{
  "id": 5657082955040122,
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
Date: Thu, 21 Mar 2019 12:49:38 GMT
x-road-id: dcaaa3a2-a158-41e1-8775-309848052358
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: VCNZdwTxl7m3XC6Mpfw1H6qJUtBcm3Y6tfCvg5b3W/fb2RRXsLF9wftR3u6ElclE+RFaiAN/OkSz02fAYbNKaw==
Content-Length: 0
```