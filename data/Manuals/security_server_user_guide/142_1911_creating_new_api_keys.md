#### 19.1.1 Creating new API keys

A new API key is created with a `POST` request to `/api/v1/api-keys`. Message body must contain the roles to be
associated with the key. Server responds with data that contains the actual API key. After this point the key
cannot be retrieved, as it is not stored in plaintext.

```bash
curl -X POST -u <user>:<password> https://localhost:4000/api/v1/api-keys --data '["XROAD_SECURITYSERVER_OBSERVER","XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k
{
  "roles": [
    "XROAD_REGISTRATION_OFFICER",
    "XROAD_SECURITYSERVER_OBSERVER"
  ],
  "id": 61,
  "key": "23bc57cd-b1ba-4702-9657-8d53e335c843"
}

```

In this example the created key was `23bc57cd-b1ba-4702-9657-8d53e335c843`.