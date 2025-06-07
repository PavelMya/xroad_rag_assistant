### 6.5 DELETE Request and Response

REQUEST

| Service       | Method | Description            | Parameters                        |
|:--------------|:-------|:-----------------------|:--------------------------------- |
| /pets/{petId} | DELETE | Deletes a pet          | petId - Pet id to delete          |

Service called directly

```bash
curl -X DELETE "https://petstore.niis.org/v2/pets/1124" -H "accept: application/json"
```

Service called through X-Road

```bash
curl -X DELETE "https://{securityserver}/r1/{serviceId}/v2/pets/1124" -H "accept: application/json"  -H "X-Road-Client: {client}"
```

Service response

```
```

Service response code

```
200
```

Service response headers

```
Date: Thu, 21 Mar 2019 12:49:38 GMT
x-road-id: 6209d61b-6ab5-4443-a09a-b8d2a7c491b2
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: lQBoldcyuI3BerjHfkleRQ45AyYoFlF7zXSN6yH/RwvTNWEcsTQM18EfqMxYfdkyGGB26oxAjAWv/AcfmZF7og==
Content-Length: 0
```