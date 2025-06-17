### 19.1 API key management operations

**Access rights:** [System Administrator](#xroad-system-administrator)

An API key is linked to a role or roles, and grants access to the operations that are allowed for that role/roles.
Separate REST endpoints exist for API key management.
API key management endpoints are authenticated to with [HTTP basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) (username and password)
or with session authentication (for admin web application).
Basic authentication access is limited to localhost by default, but this can
be changed using System Parameters \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].