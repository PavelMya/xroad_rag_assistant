### B.2 allowedMethods Response

`curl -H "accept: application/json" -H "X-Road-Client:INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1" "https://SECURITYSERVER:443/r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/allowedMethods"`

```json
{
  "service": [
    {
      "member_class": "CLASS2",
      "member_code": "MEMBER2",
      "object_type": "SERVICE",
      "service_code": "payloadgen",
      "service_type": "OPENAPI",
      "subsystem_code": "SUBSYSTEM2",
      "xroad_instance": "INSTANCE",
      "endpoint_list": [
        {
          "method": "GET",
          "path": "/pet/findByStatus"
        },
        {
          "method": "GET",
          "path": "/pet/findByTags"
        },
        {
          "method": "GET",
          "path": "/pet/*"
        }
      ]
    }
  ]
}
```