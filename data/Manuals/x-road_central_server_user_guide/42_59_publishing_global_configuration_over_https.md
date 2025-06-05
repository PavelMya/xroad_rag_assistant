### 5.9 Publishing global configuration over HTTPS

Starting from version 7.4.0, the Central Server supports publishing global configuration over HTTP and HTTPS. Instead, before version 7.4.0, only HTTP was supported.

Starting from version 7.4.0, a new private key and a self-signed TLS certificate are created automatically when installing a new Central Server or upgrading an existing installation from an older version. After the installation or upgrade, the Central Server Administrator must manually apply for a TLS certificate from a trusted Certificate Authority (CA) and then configure the certificate. The CA must be trusted by the Security Server's Java installation. More information about configuring the TLS certificate on the Central Server is available in the Central Server Installation Guide [CSI](#13-references).

Applying for a TLS certificate issued by a trusted CA is required, because the Security Server does not trust the new automatically generated self-signed certificate by default. The Security Server supports disabling certificate verification, but disabling it in production environments is not recommended. More information is available in the `[configuration-client]` section of the System Parameters User Guide [UG-SYSPAR](#13-references).

> **NOTE**: When upgrading from a version < 7.4.0 to a version 7.4.*, the configuration anchor must be re-generated and imported to all the Security Servers to enable downloading global configuration over HTTPS.

> **NOTE**: Starting from version 7.5.0, it's not required to re-generate and import the configuration anchor to all the Security Servers to enable downloading global configuration over HTTPS.