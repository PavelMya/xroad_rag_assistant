#### 17.1.4 Revoking API keys

An API key can be revoked with a `DELETE` request to `/api/v1/api-keys/{id}`. Server responds with `HTTP 200` if
revocation was successful and `HTTP 404` if key did not exist.

```bash
curl -X DELETE -u <user>:<password> https://localhost:4000/api/v1/api-keys/5  -k

```