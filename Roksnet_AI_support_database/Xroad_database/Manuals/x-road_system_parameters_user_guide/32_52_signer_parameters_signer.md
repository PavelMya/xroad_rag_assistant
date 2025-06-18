### 5.2 Signer parameters: `[signer]`

| **Name**                       | **Default value**                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ocsp-response-retrieval-active | false  _(see Description for more information)_ | This property is used as an override to deactivate periodic OCSP-response retrieval for components that don't need that functionality, but still use signer.  Values:  `false` - OCSP-response retrieval jobs are never scheduled  `true` - periodic OCSP-response retrieval is active based on ocspFetchInterval. **Note that if the entire property is missing, it is interpreted as true.**   This property is delivered as an override and only for the components where the OCSP-response retrieval jobs need to be deactivated. The property is missing for components that require OCSP-response retrieval to be activated. |
| ocsp-cache-path                | /var/cache/xroad                                     | Absolute path to the directory where the cached OCSP responses are stored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| enforce-token-pin-policy       | false                                                | Controls enforcing the token pin policy. When set to true, software token pin is required to be at least 10 ASCII characters from at least tree character classes (lowercase letters, uppercase letters, digits, special characters). (since version 6.7.7)                                                                                                                                                                                                                                                                                                                                                                                                      |

[1] Default value for proxy.client-tls-ciphers.
> TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
> TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,
> TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
> TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,
> TLS_DHE_RSA_WITH_AES_128_GCM_SHA256,
> TLS_DHE_RSA_WITH_AES_128_CBC_SHA256,
> TLS_DHE_RSA_WITH_AES_256_CBC_SHA256,
> TLS_DHE_RSA_WITH_AES_256_GCM_SHA384

[2] Default value for proxy.xroad-tls-ciphers.
> TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,
> TLS_DHE_RSA_WITH_AES_256_CBC_SHA256,
> TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384

> (see [*https://docs.oracle.com/en/java/javase/21/docs/specs/security/standard-names.html#jsse-cipher-suite-names*](https://docs.oracle.com/en/java/javase/21/docs/specs/security/standard-names.html#jsse-cipher-suite-names) for possible values)
>
> Note. OpenJDK 8 on RHEL 7 supports ECDHE key agreement protocol starting from RHEL 7.3. In RHEL 7 versions prior to RHEL 7.3 only DHE cipher suites are supported.