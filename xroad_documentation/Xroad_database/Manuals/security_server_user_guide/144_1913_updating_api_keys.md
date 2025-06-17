#### 19.1.3 Updating API keys

An existing API key is updated with a `PUT` request to `/api/v1/api-keys/{id}`. Message body must contain the roles to be
associated with the key. Server responds with data that contains the key id and roles associated with the key.

```bash
curl -X PUT -u : https://localhost:4000/api/v1/api-keys/60 --data '["XROAD_SECURITYSERVER_OBSERVER","XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k
{
  "id": 60,
  "roles": [
    "XROAD_REGISTRATION_OFFICER",
    "XROAD_SECURITYSERVER_OBSERVER"
  ]
}

```

#### 19.1.4 Revoking API keys

An API key can be revoked with a `DELETE` request to `/api/v1/api-keys/{id}`. Server responds with `HTTP 200` if
revocation was successful and `HTTP 404` if key did not exist.

```bash
curl -X DELETE -u : https://localhost:4000/api/v1/api-keys/60  -k

```