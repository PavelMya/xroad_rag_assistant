#### 17.1.1 Creating new API keys

A new API key is created with a `POST` request to `/api/v1/api-keys`. Message body must contain the roles to be
associated with the key. Server responds with data that contains the actual API key. After this point the key
cannot be retrieved, as it is not stored in plaintext.

```bash
curl -X POST -u <user>:<password> https://localhost:4000/api/v1/api-keys --data '["XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k
{
    "id": 5,
    "key": "68117d38-8613-40b4-a9ff-5afe5ea4d27b",
    "roles": [
        "XROAD_REGISTRATION_OFFICER"
    ]
}

```

In this example the created key was `68117d38-8613-40b4-a9ff-5afe5ea4d27b`.