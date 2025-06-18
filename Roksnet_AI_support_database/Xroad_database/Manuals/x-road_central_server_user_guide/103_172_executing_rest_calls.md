### 17.2 Executing REST calls

**Access rights:** Depends on the API.

Once a valid API key has been created, it is used by providing an `Authorization: X-Road-ApiKey token=` HTTP
header in the REST calls. For example

```bash
curl --header "Authorization: X-Road-ApiKey token=ff6f55a8-cc63-4e83-aa4c-55f99dc77bbf" "https://localhost:4000/api/v1/clients" -k
{
    "clients": [
        {
            "client_id": {
                "instance_id": "CS",
                "type": "MEMBER",
                "member_class": "ORG",
                "member_code": "999",
                "encoded_id": "CS:ORG:999"
            },
            "member_name": "Foo Name"
        },
...
```

The available APIs are documented in OpenAPI specification \[[REST_UI-API](#Ref_REST_UI-API)\]. Access rights for different APIs follow the same rules
as the corresponding UI operations.
Access to regular APIs is allowed from all IP addresses by default, but this can
be changed using System Parameters \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].