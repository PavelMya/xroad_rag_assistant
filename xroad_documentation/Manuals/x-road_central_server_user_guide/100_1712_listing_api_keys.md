#### 17.1.2 Listing API keys

Existing API keys can be listed with a `GET` request to `/api/v1/api-keys`. This lists all keys, regardless of who has created them.

```bash
curl -X GET -u : https://localhost:4000/api/v1/api-keys -k
[
...
    {
        "id": 5,
        "roles": [
            "XROAD_REGISTRATION_OFFICER"
        ]
    },
    {
        "id": 6,
...
]

```

You can also retrieve a single API key with a `GET` request to `/api/v1/api-keys/{id}`.

```bash
curl -X GET -u : https://localhost:4000/api/v1/api-keys/59 -k
{
    "id": 5,
    "roles": [
        "XROAD_REGISTRATION_OFFICER"
    ]
}

```