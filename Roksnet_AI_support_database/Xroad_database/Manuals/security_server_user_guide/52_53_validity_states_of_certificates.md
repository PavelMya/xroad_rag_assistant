### 5.3 Validity States of Certificates

Validity states indicate if and how a certificate can be used independent of the X-Road system. In the "Keys and Certificates" view, the certificate's validity states are displayed in the "OCSP" column. Validity states (except "Disabled") are displayed for certificates that are in the "Registered" registration state.

A Security Server certificate can be in one of the following validity states.

-   **Unknown** (validity information missing) – the certificate does not have a valid OCSP response (the OCSP response validity period is set by the X-Road governing authority) or the last OCSP response was either "unknown" (the responder doesn't know about the certificate being requested) or an error.

-   **Suspended** – the last OCSP response about the certificate was "suspended".

-   **Good** (valid) – the last OCSP response about the certificate was "good". Only certificates in the "good" (valid) state can be used to sign messages or establish a connection between Security Servers.

-   **Expired** – the certificate's validity end date has passed. The certificate is not active and OCSP queries are not performed about it.

-   **Revoked** – the last OCSP response about the certificate was "revoked". The certificate is not active and OCSP queries are not performed about it.

-   **Disabled** – the user has marked the certificate as disabled. The certificate is not active and OCSP queries are not performed about it.