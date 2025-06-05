### B.1 listMethods Response

`curl -H "accept: application/json" -H "X-Road-Client:INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1" "https://SECURITYSERVER:443/r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/listMethods"`

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
          "method": "PUT",
          "path": "/pet"
        },
        {
          "method": "POST",
          "path": "/pet"
        },
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
        },
        {
          "method": "POST",
          "path": "/pet/*"
        },
        {
          "method": "DELETE",
          "path": "/pet/*"
        },
        {
          "method": "POST",
          "path": "/pet/*/uploadImage"
        },
        {
          "method": "GET",
          "path": "/store/inventory"
        },
        {
          "method": "POST",
          "path": "/store/order"
        },
        {
          "method": "GET",
          "path": "/store/order/*"
        },
        {
          "method": "DELETE",
          "path": "/store/order/*"
        },
        {
          "method": "POST",
          "path": "/user"
        },
        {
          "method": "POST",
          "path": "/user/createWithList"
        },
        {
          "method": "GET",
          "path": "/user/login"
        },
        {
          "method": "GET",
          "path": "/user/logout"
        },
        {
          "method": "GET",
          "path": "/user/*"
        },
        {
          "method": "PUT",
          "path": "/user/*"
        },
        {
          "method": "DELETE",
          "path": "/user/*"
        }
      ]
    },
    {
      "member_class": "CLASS2",
      "member_code": "MEMBER2",
      "object_type": "SERVICE",
      "service_code": "kore",
      "service_type": "REST",
      "subsystem_code": "SUBSYSTEM2",
      "xroad_instance": "INSTANCE",
      "endpoint_list": [
        {
          "method": "GET",
          "path": "/school"
        },
        {
          "method": "PUT",
          "path": "/school"
        },
        {
          "method": "POST",
          "path": "/school"
        }
      ]
    }
  ]
}
```