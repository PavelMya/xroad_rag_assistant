#### 17.1.3 Updating API keys

An existing API key is updated with a `PUT` request to `/api/v1/api-keys/{id}`. Message body must contain the roles to be
associated with the key. Server responds with data that contains the key id and roles associated with the key.

```bash
curl -X PUT -u <user>:<password> https://localhost:4000/api/v1/api-keys/5 --data '["XROAD_SECURITY_OFFICER”,”XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k
{
  "id": 5,
  "roles": [
    "XROAD_SECURITY_OFFICER",
    "XROAD_REGISTRATION_OFFICER"
  ]
}

```