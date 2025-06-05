### 2.4 Authentication

In case the security server administrator has configured the connection between the service client and the security server to require authentication, requests to the *asic* service would need to be made via HTTPS.

The security server would need the certificate of the service client to be provided as part of the session, when the user makes the request to download a signed document for a message associated with this service client.