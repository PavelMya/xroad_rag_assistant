### 3.47 UC SS\_46: Revoke an API key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: Administrator revokes an existing API key using a REST API.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to revoke an API key.

**Main Success Scenario**:

1.  SS administrator sends HTTP DELETE request to delete one API key. REST client should
    - 2.1 Send request locally from the security server, remote access is forbidden (by default)
      - see UG-SYSPAR for how to override this \[[UG-SYSPAR](#Ref_UG-SYSPAR)\]
    - 2.2 Send request to URL `https://localhost:4000/api/v1/api-keys/{id}`,
    where `{id}` is the id of the key to be deleted.
    - 2.3 Accept REST API's self-signed SSL certificate
    - 2.4 Provide credentials of an SS administrator with role XROAD_SYSTEM_ADMINISTRATOR,
    using [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
    - Example using "curl" command: `curl -X DELETE -u : https://localhost:4000/api/v1/api-keys/63 -k`

2.  System deletes the key and it cannot be used for authentication anymore. System responds with HTTP 200.

**Extensions**:

- 1a. SS administrator provides invalid credentials or credentials for a user who does not have XROAD_SYSTEM_ADMINISTRATOR
  role
    - 1a.1. System responds with HTTP 401 or HTTP 403
- 1b. SS administrator sends request from a remote server
    - 1b.1. System responds with HTTP 401 (unless remote access is allowed, see \[[UG-SYSPAR](#Ref_UG-SYSPAR)\])
- 1c. SS administrator tries to revoke a key that does not exist
    - 1c.1. System responds with HTTP 404

**Related information:** -