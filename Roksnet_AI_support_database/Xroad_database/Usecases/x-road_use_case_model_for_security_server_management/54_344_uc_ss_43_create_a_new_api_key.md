### 3.44 UC SS\_43: Create a new API key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: Administrator creates a new API key, to be used
for authentication when executing REST API calls to update server configuration.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to create a new API key.

**Main Success Scenario**:

1.  SS administrator decides which roles the new API key should be linked to. Possible roles are
    - XROAD_SECURITY_OFFICER
    - XROAD_REGISTRATION_OFFICER
    - XROAD_SERVICE_ADMINISTRATOR
    - XROAD_SYSTEM_ADMINISTRATOR
    - XROAD_SECURITYSERVER_OBSERVER

2.  SS administrator sends HTTP POST request to create a new API key. REST client should
    - 2.1 Send request locally from the security server, remote access is forbidden (by default)
      - see UG-SYSPAR for how to override this \[[UG-SYSPAR](#Ref_UG-SYSPAR)\]
    - 2.2 Send request to URL `https://localhost:4000/api/v1/api-keys`
    - 2.3 Accept REST API's self-signed SSL certificate
    - 2.4 Provide credentials of an SS administrator with role XROAD_SYSTEM_ADMINISTRATOR,
    using [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
    - 2.5 Provide roles to link to API key, with message body containing the role names in a JSON array of strings
    - 2.6 Define correct content type with HTTP header `Content-Type: application/json`
    - Example using "curl" command: `curl -X POST -u : https://localhost:4000/api/v1/api-keys --data '["XROAD_SERVICE_ADMINISTRATOR","XROAD_REGISTRATION_OFFICER"]' --header "Content-Type: application/json" -k`

3.  System creates a new API key and responds with a JSON message containing details of the key:
    - 3.1 API key id with name `id`
    - 3.2 Roles linked to key, with name `roles`, in an array of strings
    - 3.3 Actual API key with name `key`
    - Example:

```json
{
  "roles": [
    "XROAD_REGISTRATION_OFFICER",
    "XROAD_SERVICE_ADMINISTRATOR"
  ],
  "id": 63,
  "key": "4366c766-cfd0-423f-84d5-ae1932d00b6a"
}
```
4.  SS administrator stores the API key in safe place. Key is shown only in this response, and cannot be retrieved
    later. API key should be kept safe, as it provides access to all REST API users who know the key.

**Extensions**:

- 2a. SS administrator provides invalid credentials or credentials for a user who does not have XROAD_SYSTEM_ADMINISTRATOR
  role
    - 2a.1. System responds with HTTP 401 or HTTP 403
- 2b. SS administrator sends request from a remote server
    - 2b.1. System responds with HTTP 401 (unless remote access is allowed, see \[[UG-SYSPAR](#Ref_UG-SYSPAR)\])

**Related information:** -