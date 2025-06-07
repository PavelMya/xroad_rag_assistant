### 6.2 GET Request and Response

REQUEST

| Service       | Method | Description     | Parameters                  |
|:--------------|:-------|:----------------|:----------------------------|
| /pets/{petId} | GET    | Finds pet by ID | petId - ID of pet to return |

Service called directly

```bash
curl -X GET "https://petstore.niis.org/v2/pets/1124" -H "accept: application/json"
```

Service called through X-Road

```bash
curl -X GET "https://{securityserver}/r1/{serviceId}/v2/pets/1124" -H "accept: application/json" -H "X-Road-Client: {client}"
```

Service response

```json
{
  "id": 1124,
  "name": "Siddu",
  "photoUrls": [],
  "tags": [],
  "status": "Offline"
}
```

Service response code

```
200
```

Service response headers

```
Content-Type: application/json;charset=utf-8
Date: Thu, 21 Mar 2019 12:36:39 GMT
x-road-id: 29f4d011-ef17-4f2f-9bb1-0452ce17d3f5
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: Xvx9V2U5c5RhDUiXpVLtW7L8vTd5cM2IOBU2n9efEk7/m3ECKyGAp7yTpJpTWpo6HcmwSaGO+cinxMVKjxJTOQ==
Content-Length: 1148
```