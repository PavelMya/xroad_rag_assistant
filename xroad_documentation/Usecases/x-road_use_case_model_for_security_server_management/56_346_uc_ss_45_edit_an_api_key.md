### 3.46 UC SS\_45: Edit an API key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: Administrator edits an existing API key using a REST API.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to update roles associated with an existing API key.

**Main Success Scenario**:

1.  SS administrator decides which roles the new API key should be linked to. Possible roles are
    - XROAD_SECURITY_OFFICER
    - XROAD_REGISTRATION_OFFICER
    - XROAD_SERVICE_ADMINISTRATOR
    - XROAD_SYSTEM_ADMINISTRATOR
    - XROAD_SECURITYSERVER_OBSERVER

2.  SS administrator sends HTTP PUT request to update an API key. REST client should
    - 2.1 Send request locally from the security server, remote access is forbidden
    - 2.2 Send request to URL `https://localhost:4000/api/v1/api-keys/{id}`,
    where `{id}` is the id of the key to be updated.
    - 2.3 Accept REST API's self-signed SSL certificate
    - 2.4 Provide credentials of an SS administrator with role XROAD_SYSTEM_ADMINISTRATOR,
    using [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
    - 2.5 Provide roles to link to API key, with message body containing the role names in a JSON array of strings
    - 2.6 Define correct content type with HTTP header `Content-Type: application/json`
    - Example using "curl" command: `curl -X PUT -u : https://localhost:4000/api/v1/api-keys/63 --data '["XROAD_SERVICE_ADMINISTRATOR","XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k`

3.  System updates the API key and responds with a JSON message containing details of the key:
    - 3.1 API key id with name `id`
    - 3.2 Roles linked to key, with name `roles`, in an array of strings
    - Example:

```
{
  "roles": [
    "XROAD_REGISTRATION_OFFICER",
    "XROAD_SERVICE_ADMINISTRATOR"
  ],
  "id": 63
}
```

**Extensions**:

- 1a. SS administrator provides invalid credentials or credentials for a user who does not have XROAD_SYSTEM_ADMINISTRATOR
  role
    - 1a.1. System responds with HTTP 401 or HTTP 403
- 1b. SS administrator sends request from a remote server
    - 1b.1. System responds with HTTP 403
- 1c. SS administrator tries to update a key that does not exist
    - 1c.1. System responds with HTTP 404

**Related information:** -