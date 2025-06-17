### 6.6 POST Request with Attachments and Response

REQUEST

| Service              | Method | Description            | Parameters                        |
|:---------------------|:-------|:-----------------------|:--------------------------------- |
| /pets/{petId}/images | POST   | uploads an image       |• petId - ID of pet to update  • additionalMetadata - Additional data to pass to server  • file - file to upload|

Service called directly

```bash
curl -X POST "https://petstore.niis.org/v2/pets/1124/images" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@A-fluffy-cat-looking-funny-surprised-or-concerned.jpg;type=image/jpeg"
```

Service called through X-Road

```bash
curl -X POST "https://{securityserver}/r1/{serviceId}/v2/pets/1124/images" -H "accept: application/json" -H "Content-Type: multipart/form-data" -H "X-Road-client: {client}" -F "file=@A-fluffy-cat-looking-funny-surprised-or-concerned.jpg;type=image/jpeg"
```

Service response

```json
{
  "code": 200,
  "type": null,
  "message": "additionalMetadata: null\nFile uploaded to ./file, 170025 bytes"
}
```

Service response code

```
200
```

Service response headers

```
Content-Type: application/json;charset=utf-8
Date: Thu, 21 Mar 2019 13:02:29 GMT
x-road-id: 86e081a6-ec16-4b8d-b729-963f9659a80c
x-road-client: DEV/COM/222/TESTCLIENT
x-road-service: DEV/COM/222/TESTSERVICE/petstore
x-road-request-id: f92591a3-6bf0-49b1-987b-0dd78c034cc3
x-road-request-hash: EycIkZAz4WMvbKgnBvd0wUcN4A4w0RZMvugD36ZJ2PpwwGZuMGfxCoO4C0ZC3c4LBGF0rh61vunL3ssZV6TB3Q==
Content-Length: 100
```