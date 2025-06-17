### 3.45 UC SS\_44: List API keys

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: Administrator lists existing API keys using a REST API.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to list existing new API keys.

**Main Success Scenario**:

1.  SS administrator sends HTTP GET request to list all API keys. REST client should
    - 2.1 Send request locally from the security server, remote access is forbidden (by default)
      - see UG-SYSPAR for how to override this \[[UG-SYSPAR](#Ref_UG-SYSPAR)\]
    - 2.2 Send request to URL `https://localhost:4000/api/v1/api-keys`
    - 2.3 Accept REST API's self-signed SSL certificate
    - 2.4 Provide credentials of an SS administrator with role XROAD_SYSTEM_ADMINISTRATOR,
    using [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
    - Example using "curl" command: `curl -X GET -u : https://localhost:4000/api/v1/api-keys -k`

2.  System returns list of API keys in an JSON array containing items with details of the keys:
    - 3.1 API key id with name `id`
    - 3.2 Roles linked to key, with name `roles`, in array of strings
    - System does *not* return the actual API keys
    - Example:

```
[
  {
    "id": 62,
    "roles": [
      "XROAD_REGISTRATION_OFFICER",
      "XROAD_SECURITYSERVER_OBSERVER",
      "XROAD_SERVICE_ADMINISTRATOR"
    ]
  },
  {
    "id": 63,
    "roles": [
      "XROAD_REGISTRATION_OFFICER",
      "XROAD_SERVICE_ADMINISTRATOR"
    ]
  }
]
```

**Extensions**:

- 1a. SS administrator provides invalid credentials or credentials for a user who does not have XROAD_SYSTEM_ADMINISTRATOR
  role
    - 1a.1. System responds with HTTP 401 or HTTP 403
- 1b. SS administrator sends request from a remote server
    - 2b.1. System responds with HTTP 401 (unless remote access is allowed, see \[[UG-SYSPAR](#Ref_UG-SYSPAR)\])

**Related information:** -