### 2.3 JSON Web Tokens and the `securityToken` attribute `tokenType`
When transferring JSON Web Tokens, the URI attribute `tokenType` should have the value `urn:ietf:params:oauth:token-type:jwt`
which is the URI content type for JWT content specified by [section 10.2.1.](https://tools.ietf.org/html/rfc7519#section-10.2.1)
of the JSON Web Token RFC \[[JWT-RFC](#Ref_JWT-RFC)\]. However, using this value for the `tokenType` is not enforced in any way. The JWT content is not
currently validated or verified by the security server.

### 2.4 Message headers
 This section describes the additional SOAP headers that are added by this extension.

|Field | Mandatory/Optional | Description |
|-------------|-------------|-------------|
| securityToken | Optional | The security token |