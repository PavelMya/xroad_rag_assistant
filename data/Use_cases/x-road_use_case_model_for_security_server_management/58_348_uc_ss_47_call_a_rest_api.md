### 3.48 UC SS\_47: Call a REST API

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: Administrator performs a configuration action using a REST API.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to read or update configuration using a REST API.

**Main Success Scenario**:

1.  SS administrator sends a REST request to perform some kind of configuration action. REST client should
    - 2.1 Send request from anywhere, remote access is not forbidden (by default)
      - see UG-SYSPAR for how to override this \[[UG-SYSPAR](#Ref_UG-SYSPAR)\]
    - 2.2 Send request to URL corresponding to the desired action,
     for example `https://<security-server-address>:4000/api/v1/clients` to list clients.
    - 2.3 Use HTTP method corresponding to the desired action,
     for example HTTP GET to list clients.
    - 2.4 Accept REST API's self-signed SSL certificate
    - 2.5 Provide API key (created in [UC SS\_43](#344-uc-ss_43-create-a-new-api-key)) in HTTP header
    `Authorization: X-Road-ApiKey token=<api key>`
    - 2.6 Provide required message, if any, in HTTP body
    - 2.7 Specify correct content type for the body, if any, with HTTP header such as `Content-Type: application/json`
    - Example using "curl" command: `curl --header "Authorization: X-Road-apikey token=<api key>" "https://<security-server-address>:4000/api/v1/clients" -k`

2.  System performs the desired action. System responds with HTTP 200. System returns the results of the operation,
    if any, in HTTP body

**Extensions**:

- 1a. SS administrator provides an invalid or revoked API key
    - 1a.1. System responds with HTTP 401
- 1b. SS administrator provides an API key which is not linked to roles that are required to execute the operation
    - 1b.1. System responds with HTTP 403
- 1c. There is a problem when executing the operation
    - 1c.1. System responds with a HTTP status corresponding to the failure (documented in OpenAPI specification)

**Related information:**

The available endpoints, and the details of them, are specified in more detail in OpenAPI specification and
REST API guidelines (TBD). Access rights for different REST API endpoints follow the same rules as the corresponding UI operations.