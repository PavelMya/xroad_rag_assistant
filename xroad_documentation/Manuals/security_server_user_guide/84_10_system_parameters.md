## 10 System Parameters

The Security Server system parameters are:

-   **Security Server address.** The Security Server address.

-   **Configuration anchor's information.** The configuration anchor contains data that is used to periodically download signed configuration from the Central Server and to verify the signature of the downloaded configuration.

-   **Timestamping service information.** Timestamping is used to preserve the evidential value of messages exchanged over X-Road.

-   **Approved Certificate Authorities.** A read-only list of approved certificate authorities (defined in the global configuration). The Security Server trusts authentication and signing certificates signed by the listed authorities.

-   **The internal TLS key and certificate.** The internal TLS certificate is used to establish a TLS connection with the Security Server client's information system if the "HTTPS" connection method is chosen for the client's servers.