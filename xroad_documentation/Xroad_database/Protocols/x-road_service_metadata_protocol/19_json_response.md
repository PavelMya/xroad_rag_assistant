#### JSON Response
`curl -H "Accept: application/json" http://SECURITYSERVER/listClients`

```json
{
  "member": [
    {
      "id": {
        "member_class": "GOV",
        "member_code": "TS1OWNER",
        "object_type": "MEMBER",
        "xroad_instance": "AA"
      },
      "name": "TS1 Owner"
    },
    {
      "id": {
        "member_class": "GOV",
        "member_code": "TS2OWNER",
        "object_type": "MEMBER",
        "xroad_instance": "AA"
      },
      "name": "TS2 Owner"
    },
    {
      "id": {
        "member_class": "ENT",
        "member_code": "CLIENT1",
        "object_type": "MEMBER",
        "xroad_instance": "AA"
      },
      "name": "Client One"
    },
    {
      "id": {
        "member_class": "ENT",
        "member_code": "CLIENT1",
        "subsystem_code": "sub",
        "object_type": "SUBSYSTEM",
        "xroad_instance": "AA"
      },
      "name": "Client One",
      "subsystem_name": "Client One Sub"
    }
  ]
}
```